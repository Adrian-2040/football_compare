from contextlib import closing

from app.database import get_connection
from app.models import Player


class PlayerRepository:
    """Jedyne miejsce, ktore rozmawia z baza. Reszta aplikacji nie zna SQL-a."""

    def __init__(self, database_path):
        self._database_path = database_path

    def get_all(self):
        with closing(get_connection(self._database_path)) as connection:
            rows = connection.execute("SELECT * FROM players ORDER BY name").fetchall()
        return [self._row_to_player(row) for row in rows]

    def get_by_id(self, player_id):
        with closing(get_connection(self._database_path)) as connection:
            row = connection.execute(
                "SELECT * FROM players WHERE id = ?", (player_id,)
            ).fetchone()
        if row is None:
            return None
        return self._row_to_player(row)

    @staticmethod
    def _row_to_player(row):
        # Zamienia wiersz z bazy na obiekt Player
        return Player(
            id=row["id"],
            name=row["name"],
            club=row["club"],
            position=row["position"],
            appearances=row["appearances"],
            goals=row["goals"],
            assists=row["assists"],
        )