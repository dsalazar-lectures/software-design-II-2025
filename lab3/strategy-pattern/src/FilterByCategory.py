from typing import List
from FilterStrategy import FilterStrategy
from Recipe import Recipe

class FilterByCategory(FilterStrategy):
    def filter(self, recetas: List[Recipe], criteria: str):
        # criteriaLower = criteria.lower().strip()
        return [r for r in recetas if r.category.lower().strip() == criteria.lower().strip()]