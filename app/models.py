"""
models.py (modele)

Tu są klasy, które tylko trzymają dane.
Player - jeden piłkarz.
StatsComparison - wynik porównania dwóch piłkarzy.
Metoda to_dict zamienia obiekt na słownik, żeby API mogło go wysłać jako JSON.
"""


class Player:
    def __init__(self, id, name, club, position, appearances, goals, assists):
        self.id = id
        self.name = name
        self.club = club
        self.position = position
        self.appearances = appearances
        self.goals = goals
        self.assists = assists

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "club": self.club,
            "position": self.position,
            "appearances": self.appearances,
            "goals": self.goals,
            "assists": self.assists,
        }


class StatsComparison:
    def __init__(self, first, second, appearances_difference,
                 goals_difference, assists_difference):
        self.first = first
        self.second = second
        self.appearances_difference = appearances_difference
        self.goals_difference = goals_difference
        self.assists_difference = assists_difference

    def to_dict(self):
        return {
            "first": self.first.to_dict(),
            "second": self.second.to_dict(),
            "appearances_difference": self.appearances_difference,
            "goals_difference": self.goals_difference,
            "assists_difference": self.assists_difference,
        }