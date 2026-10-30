from app.exceptions import InvalidSelectionError, PlayerNotFoundError
from app.models import StatsComparison


class ComparisonService:
    """Odpowiada tylko za porownywanie: sprawdza dane i liczy roznice."""

    def __init__(self, repository):
        self._repository = repository

    def compare(self, first_id, second_id):
        self._validate_ids(first_id, second_id)
        first = self._find_player(first_id)
        second = self._find_player(second_id)

        return StatsComparison(
            first=first,
            second=second,
            appearances_difference=first.appearances - second.appearances,
            goals_difference=first.goals - second.goals,
            assists_difference=first.assists - second.assists,
        )

    @staticmethod
    def _validate_ids(first_id, second_id):
        # Sprawdza, czy uzytkownik wybral dwoch roznych pilkarzy
        if first_id is None or second_id is None:
            raise InvalidSelectionError("Select both players")
        if first_id == second_id:
            raise InvalidSelectionError("Select two different players")

    def _find_player(self, player_id):
        player = self._repository.get_by_id(player_id)
        if player is None:
            raise PlayerNotFoundError(player_id)
        return player