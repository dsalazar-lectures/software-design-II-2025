from typing import List
from FilterStrategy import FilterStrategy
from Recipe import Recipe

class FilterByIngredient(FilterStrategy):
    def filter(self, recetas: List[Recipe], criteria: str):
        resultado = []
        for r in recetas:
            if criteria.lower().strip() in r.ingredients.lower():
                resultado.append(r)
        return resultado