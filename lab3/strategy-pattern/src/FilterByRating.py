from FilterStrategy import FilterStrategy
from Recipe import Recipe
from typing import List

class FilterByRating(FilterStrategy):
    def filter(self, recetas : List, criteria: float):
        return [r for r in recetas if r.rating == criteria]