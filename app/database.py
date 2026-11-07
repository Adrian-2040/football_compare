"""
database.py (baza danych)

Ten plik tworzy bazę SQLite (plik football.db) i wstawia 30 piłkarzy.
Piłkarze są wstawiani tylko wtedy, gdy tabela jest pusta.
Dane są przykładowe, nie z oficjalnych statystyk.
"""

import sqlite3

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

# (imię, klub, pozycja, występy, gole, asysty)
SAMPLE_PLAYERS = [
    # Napastnicy
    ("Robert Lewandowski", "FC Barcelona", "Napastnik", 50, 40, 8),
    ("Lionel Messi", "Inter Miami", "Napastnik", 45, 30, 20),
    ("Erling Haaland", "Manchester City", "Napastnik", 48, 38, 6),
    ("Kylian Mbappe", "Real Madrid", "Napastnik", 52, 42, 10),
    ("Harry Kane", "Bayern Monachium", "Napastnik", 49, 44, 12),
    ("Vinicius Junior", "Real Madrid", "Napastnik", 50, 22, 15),
    ("Mohamed Salah", "Liverpool", "Napastnik", 51, 29, 18),
    ("Lautaro Martinez", "Inter Mediolan", "Napastnik", 47, 27, 7),
    ("Victor Osimhen", "Galatasaray", "Napastnik", 44, 26, 5),
    ("Cristiano Ronaldo", "Al-Nassr", "Napastnik", 46, 33, 9),
    # Pomocnicy
    ("Kevin De Bruyne", "SSC Napoli", "Pomocnik", 40, 8, 18),
    ("Luka Modric", "AC Milan", "Pomocnik", 42, 4, 9),
    ("Jude Bellingham", "Real Madrid", "Pomocnik", 48, 14, 10),
    ("Rodri", "Manchester City", "Pomocnik", 45, 6, 8),
    ("Pedri", "FC Barcelona", "Pomocnik", 43, 7, 11),
    ("Jamal Musiala", "Bayern Monachium", "Pomocnik", 44, 13, 12),
    ("Bruno Fernandes", "Manchester United", "Pomocnik", 50, 12, 16),
    ("Martin Odegaard", "Arsenal", "Pomocnik", 46, 10, 13),
    ("Piotr Zielinski", "Inter Mediolan", "Pomocnik", 47, 6, 8),
    ("Federico Valverde", "Real Madrid", "Pomocnik", 49, 9, 9),
    # Obrońcy
    ("Virgil van Dijk", "Liverpool", "Obrońca", 48, 4, 2),
    ("Ruben Dias", "Manchester City", "Obrońca", 44, 2, 3),
    ("Trent Alexander-Arnold", "Real Madrid", "Obrońca", 42, 3, 12),
    ("Achraf Hakimi", "Paris Saint-Germain", "Obrońca", 46, 6, 11),
    ("Alphonso Davies", "Bayern Monachium", "Obrońca", 40, 3, 8),
    ("Marquinhos", "Paris Saint-Germain", "Obrońca", 47, 5, 3),
    # Bramkarze
    ("Wojciech Szczesny", "FC Barcelona", "Bramkarz", 38, 0, 0),
    ("Thibaut Courtois", "Real Madrid", "Bramkarz", 40, 0, 0),
    ("Manuel Neuer", "Bayern Monachium", "Bramkarz", 36, 0, 1),
    ("Alisson Becker", "Liverpool", "Bramkarz", 39, 0, 1),
]


def init_database(database_path):
    # Tworzymy tabelę i, jeśli jest pusta, wstawiamy piłkarzy
    connection = sqlite3.connect(database_path)
    connection.execute(CREATE_TABLE_SQL)
    count = connection.execute("SELECT COUNT(*) FROM players").fetchone()[0]
    if count == 0:
        connection.executemany(INSERT_PLAYER_SQL, SAMPLE_PLAYERS)
    connection.commit()
    connection.close()