from typing import List
from specification_base import Specification
from models import Recipe


class RecipeRepository:
    """Repositorio de recetas que soporta especificaciones"""
    
    def __init__(self, recipes: List[Recipe]):
        self._recipes = recipes
    
    def find(self, specification: Specification) -> List[Recipe]:
        """Encuentra recetas que cumplan la especificación"""
        return [r for r in self._recipes if specification.is_satisfied_by(r)]
    
    def find_one(self, specification: Specification) -> Recipe:
        """Encuentra la primera receta que cumpla la especificación"""
        for recipe in self._recipes:
            if specification.is_satisfied_by(recipe):
                return recipe
        return None
    
    def count(self, specification: Specification) -> int:
        """Cuenta recetas que cumplan la especificación"""
        return len(self.find(specification))
