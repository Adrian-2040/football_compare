"""
exceptions.py (wyjątki)
Tu są nasze własne błędy.
InvalidSelectionError - użytkownik źle wybrał piłkarzy.
PlayerNotFoundError - piłkarza nie ma w bazie.
"""


class InvalidSelectionError(Exception):
    pass


class PlayerNotFoundError(Exception):
    pass