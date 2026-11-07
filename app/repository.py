"""
repository.py (repozytorium)
Tylko ten plik pyta bazę danych o piłkarzy.
"""

import sqlite3

from app.models import Player


class PlayerRepository:
    def __init__(self, database_path):
        self.database_path = database_path

    def get_all(self):
        connection = sqlite3.connect(self.database_path)
        rows = connection.execute("SELECT * FROM players ORDER BY name").fetchall()
        connection.close()

        players = []
        for row in rows:
            player = Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            players.append(player)
        return players

    def get_by_id(self, player_id):
        connection = sqlite3.connect(self.database_path)
        row = connection.execute(
            "SELECT * FROM players WHERE id = ?", (player_id,)
        ).fetchone()
        connection.close()

        if row is None:
            return None
        return Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6])