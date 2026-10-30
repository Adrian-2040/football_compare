from flask import Flask

from app.comparison_service import ComparisonService
from app.database import init_database
from app.player_service import PlayerService
from app.repository import PlayerRepository
from app.routes import main_blueprint


def create_app(database_path="football.db"):
    """Sklada aplikacje z czesci. Sciezke do bazy mozna podac z zewnatrz,
    dzieki czemu w testach uzyjemy osobnej, tymczasowej bazy."""
    app = Flask(__name__)

    init_database(database_path)
    repository = PlayerRepository(database_path)

    app.config["PLAYER_SERVICE"] = PlayerService(repository)
    app.config["COMPARISON_SERVICE"] = ComparisonService(repository)

    app.register_blueprint(main_blueprint)
    return app