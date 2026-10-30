from dataclasses import dataclass


# @dataclass sam tworzy konstruktor i inne metody, wiec klasa to tylko "pojemnik na dane".
# frozen=True oznacza, ze po utworzeniu obiektu nie mozna zmienic jego pol.
@dataclass(frozen=True)
class Player:
    id: int
    name: str
    club: str
    position: str
    appearances: int
    goals: int
    assists: int


# Wynik porownania. Roznica = statystyka pierwszego minus statystyka drugiego.
@dataclass(frozen=True)
class StatsComparison:
    first: Player
    second: Player
    appearances_difference: int
    goals_difference: int
    assists_difference: int