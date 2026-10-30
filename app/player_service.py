class PlayerService:
    """Odpowiada tylko za pobieranie listy pilkarzy."""

    def __init__(self, repository):
        # Repository dostajemy "z zewnatrz" (wstrzykiwanie zaleznosci).
        # Dzieki temu w testach mozna podstawic atrape zamiast prawdziwej bazy.
        self._repository = repository

    def get_all_players(self):
        return self._repository.get_all()