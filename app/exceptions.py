# Wlasne bledy aplikacji. Dzieki nim wiadomo, CO poszlo nie tak.


class InvalidSelectionError(ValueError):
    """Uzytkownik wybral zle dane (brak pilkarza albo ten sam dwa razy)."""


class PlayerNotFoundError(LookupError):
    """Pilkarza o podanym id nie ma w bazie."""

    def __init__(self, player_id):
        super().__init__(f"Player with id {player_id} was not found")