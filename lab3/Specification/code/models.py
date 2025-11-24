from typing import List
from enum import Enum


class DietType(Enum):
    """Tipos de dietas"""
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten_free"
    KETO = "keto"
    PALEO = "paleo"
    OMNIVORE = "omnivore"


class DifficultyLevel(Enum):
    """Niveles de dificultad"""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class MealType(Enum):
    """Tipos de comidas"""
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
    DESSERT = "dessert"


class Ingredient:
    """Representa un ingrediente"""
    
    def __init__(self, name: str, quantity: float, unit: str, calories: int = 0):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories = calories
    
    def __repr__(self):
        return f"{self.quantity} {self.unit} de {self.name}"


class Recipe:
    """Representa una receta de cocina"""
    
    def __init__(self, name: str, ingredients: List[Ingredient], 
                 preparation_time: int, difficulty: DifficultyLevel,
                 servings: int, diet_types: List[DietType],
                 meal_types: List[MealType], calories: int = 0):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time  # en minutos
        self.difficulty = difficulty
        self.servings = servings
        self.diet_types = diet_types
        self.meal_types = meal_types
        self.calories = calories if calories > 0 else sum(ing.calories for ing in ingredients)
    
    def __repr__(self):
        return f"Recipe({self.name}, {self.preparation_time}min, {self.difficulty.value})"


class Menu:
    """Representa un menú compuesto por varias recetas"""
    
    def __init__(self, name: str, recipes: List[Recipe]):
        self.name = name
        self.recipes = recipes
    
    @property
    def total_calories(self):
        return sum(recipe.calories for recipe in self.recipes)
    
    @property
    def total_preparation_time(self):
        return sum(recipe.preparation_time for recipe in self.recipes)
    
    def __repr__(self):
        return f"Menu({self.name}, {len(self.recipes)} recetas)"
