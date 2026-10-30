from dataclasses import asdict

from flask import Blueprint, current_app, jsonify, render_template, request

from app.exceptions import InvalidSelectionError, PlayerNotFoundError

# Blueprint to "paczka" adresow URL, ktora rejestrujemy w aplikacji
main_blueprint = Blueprint("main", __name__)


def _get_players():
    return current_app.config["PLAYER_SERVICE"].get_all_players()


def _compare(first_id, second_id):
    return current_app.config["COMPARISON_SERVICE"].compare(first_id, second_id)


# ---------- Strona HTML ----------

@main_blueprint.route("/")
def show_form():
    # Wejscie na http://localhost:5000/ pokazuje sam formularz
    return render_template("index.html", players=_get_players())


@main_blueprint.route("/compare")
def compare_page():
    # type=int zamienia tekst z adresu na liczbe (a przy pustej wartosci daje None)
    first_id = request.args.get("first_id", type=int)
    second_id = request.args.get("second_id", type=int)
    comparison = None
    error_message = None

    try:
        comparison = _compare(first_id, second_id)
    except (InvalidSelectionError, PlayerNotFoundError) as error:
        # Zamiast bledu serwera pokazujemy uzytkownikowi czytelny komunikat
        error_message = str(error)

    return render_template(
        "index.html",
        players=_get_players(),
        comparison=comparison,
        error_message=error_message,
    )


# ---------- API w JSON ----------

@main_blueprint.route("/api/players")
def get_players_api():
    # GET /api/players -> lista wszystkich pilkarzy
    return jsonify([asdict(player) for player in _get_players()])


@main_blueprint.route("/api/compare")
def compare_api():
    # GET /api/compare?first_id=1&second_id=2 -> porownanie dwoch pilkarzy
    first_id = request.args.get("first_id", type=int)
    second_id = request.args.get("second_id", type=int)

    try:
        comparison = _compare(first_id, second_id)
    except InvalidSelectionError as error:
        return jsonify({"error": str(error)}), 400  # 400 = zle dane od uzytkownika
    except PlayerNotFoundError as error:
        return jsonify({"error": str(error)}), 404  # 404 = nie znaleziono

    return jsonify(asdict(comparison))