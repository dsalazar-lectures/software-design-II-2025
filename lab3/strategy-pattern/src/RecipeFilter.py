from typing import List
from FilterStrategy import FilterStrategy

class RecipeFilter:
    def __init__(self, strategy = None):
        self._strategy = strategy
    
    # permite cambiar la estrategia en tiempo de ejecución
    def setStrategy(self, strategy):
        self._strategy = strategy
    
    # ejecuta la estrategia elegida
    def applyFilter(self, recipes: List, criteria):
        if self._strategy is None:
            raise ValueError("No se ha definido una estrategia de filtrado")
        return self._strategy.filter(recipes, criteria)