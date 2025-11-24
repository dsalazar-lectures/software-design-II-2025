from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Recipe:
    id: int
    name: str
    ingredients: list[str]
    author: str

    def __str__(self):
        resultado = f"Receta #{self.id}: {self.name}\n"
        resultado += f"Autor: {self.author}\n"
        resultado += "Ingredientes:\n"
        for ing in self.ingredients:
            resultado += f"  - {ing}\n"
        return resultado
    
# Interfaz DAO con CRUD  para Recetas
class RecipeDAO(ABC):

    @abstractmethod
    def create(self, name, ingredients, author):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, recipe_id):
        pass

    @abstractmethod
    def update(self, recipe_id, name=None, ingredients=None):
        pass

    @abstractmethod
    def delete(self, recipe_id):
        pass
