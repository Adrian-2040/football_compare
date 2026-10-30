import sqlite3
from contextlib import closing

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    club TEXT NOT NULL,
    position TEXT NOT NULL,
    appearances INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    assists INTEGER NOT NULL
)
"""

INSERT_PLAYER_SQL = """
INSERT INTO players (name, club, position, appearances, goals, assists)
VALUES (?, ?, ?, ?, ?, ?)
"""

# Przykladowi pilkarze (dane orientacyjne, na potrzeby projektu)
SAMPLE_PLAYERS = [
    ("Robert Lewandowski", "FC Barcelona", "Forward", 50, 40, 8),
    ("Lionel Messi", "Inter Miami", "Forward", 45, 30, 20),
    ("Erling Haaland", "Manchester City", "Forward", 48, 38, 6),
    ("Kylian Mbappe", "Real Madrid", "Forward", 52, 42, 10),
    ("Kevin De Bruyne", "SSC Napoli", "Midfielder", 40, 8, 18),
    ("Luka Modric", "AC Milan", "Midfielder", 42, 4, 9),
]


def get_connection(database_path):
    """Otwiera polaczenie z baza. row_factory pozwala brac kolumny po nazwie."""
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_database(database_path):
    """Tworzy tabele i wstawia przykladowych pilkarzy, jesli tabela jest pusta."""
    with closing(get_connection(database_path)) as connection:
        with connection:  # zapisuje zmiany (commit) po wykonaniu bloku
            connection.execute(CREATE_TABLE_SQL)
            count = connection.execute("SELECT COUNT(*) FROM players").fetchone()[0]
            if count == 0:
                connection.executemany(INSERT_PLAYER_SQL, SAMPLE_PLAYERS)