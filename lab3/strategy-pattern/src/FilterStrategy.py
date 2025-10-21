from abc import ABC, abstractmethod
from typing import List
from Recipe import Recipe

class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, recetas: List[Recipe], criteria):
        pass