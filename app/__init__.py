"""
__init__.py
Ten plik składa całą aplikację w funkcji create_app:
baza, repozytorium, serwis i adresy URL.
Ścieżkę do bazy można podać, więc w testach użyję innej bazy.
"""

from flask import Flask, jsonify, render_template, request

from app.comparison_service import ComparisonService
from app.database import init_database
from app.exceptions import InvalidSelectionError, PlayerNotFoundError
from app.repository import PlayerRepository


def create_app(database_path="football.db"):
    app = Flask(__name__)

    init_database(database_path)
    repository = PlayerRepository(database_path)
    comparison_service = ComparisonService(repository)

    # Strona główna - sam formularz
    @app.route("/")
    def show_form():
        players = repository.get_all()
        return render_template("index.html", players=players)

    # Strona z wynikiem porównania
    @app.route("/compare")
    def compare_page():
        first_id = request.args.get("first_id", type=int)
        second_id = request.args.get("second_id", type=int)
        comparison = None
        error_message = None

        try:
            comparison = comparison_service.compare(first_id, second_id)
        except InvalidSelectionError as error:
            error_message = str(error)
        except PlayerNotFoundError as error:
            error_message = str(error)

        players = repository.get_all()
        return render_template(
            "index.html",
            players=players,
            comparison=comparison,
            error_message=error_message,
        )

    # API: lista piłkarzy w JSON
    @app.route("/api/players")
    def get_players_api():
        players = []
        for player in repository.get_all():
            players.append(player.to_dict())
        return jsonify(players)

    # API: porównanie dwóch piłkarzy w JSON
    @app.route("/api/compare")
    def compare_api():
        first_id = request.args.get("first_id", type=int)
        second_id = request.args.get("second_id", type=int)

        try:
            comparison = comparison_service.compare(first_id, second_id)
        except InvalidSelectionError as error:
            return jsonify({"error": str(error)}), 400
        except PlayerNotFoundError as error:
            return jsonify({"error": str(error)}), 404

        return jsonify(comparison.to_dict())

    return app