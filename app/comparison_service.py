"""
comparison_service.py (serwis porównywania)

Tu jest najważniejsza logika projektu.
1. Sprawdzam, czy wybrano dwóch różnych piłkarzy.
2. Pobieram ich z repozytorium.
3. Odejmuję statystyki: pierwszy minus drugi.
"""

from app.exceptions import InvalidSelectionError, PlayerNotFoundError
from app.models import StatsComparison


class ComparisonService:
    def __init__(self, repository):
        self.repository = repository

    def compare(self, first_id, second_id):
        if first_id is None or second_id is None:
            raise InvalidSelectionError("Wybierz obu piłkarzy")
        if first_id == second_id:
            raise InvalidSelectionError("Wybierz dwóch różnych piłkarzy")

        first = self.repository.get_by_id(first_id)
        if first is None:
            raise PlayerNotFoundError("Nie znaleziono piłkarza o id " + str(first_id))

        second = self.repository.get_by_id(second_id)
        if second is None:
            raise PlayerNotFoundError("Nie znaleziono piłkarza o id " + str(second_id))

        return StatsComparison(
            first,
            second,
            first.appearances - second.appearances,
            first.goals - second.goals,
            first.assists - second.assists,
        )