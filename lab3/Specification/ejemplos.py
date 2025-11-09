from abc import ABC, abstractmethod
from typing import List, Set
from enum import Enum

# Ejemplo 1: Estructura Base del Patrón Specification
class Specification(ABC):
    """Interfaz base para especificaciones"""
    
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass
    
    def and_(self, other):
        return AndSpecification(self, other)
    
    def or_(self, other):
        return OrSpecification(self, other)
    
    def not_(self):
        return NotSpecification(self)


class AndSpecification(Specification):
    """Combina dos especificaciones con AND lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)


class OrSpecification(Specification):
    """Combina dos especificaciones con OR lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)


class NotSpecification(Specification):
    """Niega una especificación"""
    
    def __init__(self, spec: Specification):
        self.spec = spec
    
    def is_satisfied_by(self, candidate):
        return not self.spec.is_satisfied_by(candidate)


# Modelos del Dominio: Ingrediente, Receta, Menú
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


# Ejemplo 2: Especificaciones para Recetas
class HasIngredientSpec(Specification):
    """Verifica si la receta contiene un ingrediente específico"""
    
    def __init__(self, ingredient_name: str):
        self.ingredient_name = ingredient_name.lower()
    
    def is_satisfied_by(self, recipe):
        return any(ing.name.lower() == self.ingredient_name for ing in recipe.ingredients)


class HasAllIngredientsSpec(Specification):
    """Verifica si la receta contiene todos los ingredientes especificados"""
    
    def __init__(self, ingredient_names: List[str]):
        self.ingredient_names = [name.lower() for name in ingredient_names]
    
    def is_satisfied_by(self, recipe):
        recipe_ingredients = [ing.name.lower() for ing in recipe.ingredients]
        return all(name in recipe_ingredients for name in self.ingredient_names)


class AvoidIngredientSpec(Specification):
    """Verifica que la receta NO contenga un ingrediente específico (alergias)"""
    
    def __init__(self, ingredient_name: str):
        self.ingredient_name = ingredient_name.lower()
    
    def is_satisfied_by(self, recipe):
        return not any(ing.name.lower() == self.ingredient_name for ing in recipe.ingredients)


class PreparationTimeSpec(Specification):
    """Verifica si el tiempo de preparación está dentro de un límite"""
    
    def __init__(self, max_minutes: int):
        self.max_minutes = max_minutes
    
    def is_satisfied_by(self, recipe):
        return recipe.preparation_time <= self.max_minutes


class DifficultySpec(Specification):
    """Verifica el nivel de dificultad de la receta"""
    
    def __init__(self, difficulty: DifficultyLevel):
        self.difficulty = difficulty
    
    def is_satisfied_by(self, recipe):
        return recipe.difficulty == self.difficulty


class CaloriesRangeSpec(Specification):
    """Verifica si las calorías están dentro de un rango"""
    
    def __init__(self, min_calories: int, max_calories: int):
        self.min_calories = min_calories
        self.max_calories = max_calories
    
    def is_satisfied_by(self, recipe):
        return self.min_calories <= recipe.calories <= self.max_calories


class DietTypeSpec(Specification):
    """Verifica si la receta es compatible con un tipo de dieta"""
    
    def __init__(self, diet_type: DietType):
        self.diet_type = diet_type
    
    def is_satisfied_by(self, recipe):
        return self.diet_type in recipe.diet_types


class MealTypeSpec(Specification):
    """Verifica el tipo de comida (desayuno, almuerzo, cena, etc.)"""
    
    def __init__(self, meal_type: MealType):
        self.meal_type = meal_type
    
    def is_satisfied_by(self, recipe):
        return self.meal_type in recipe.meal_types


class ServingsSpec(Specification):
    """Verifica si la receta sirve para un número específico de personas"""
    
    def __init__(self, min_servings: int, max_servings: int):
        self.min_servings = min_servings
        self.max_servings = max_servings
    
    def is_satisfied_by(self, recipe):
        return self.min_servings <= recipe.servings <= self.max_servings


class AvailableIngredientsSpec(Specification):
    """Verifica si todos los ingredientes de la receta están disponibles en la despensa"""
    
    def __init__(self, available_ingredients: Set[str]):
        self.available_ingredients = {ing.lower() for ing in available_ingredients}
    
    def is_satisfied_by(self, recipe):
        recipe_ingredients = {ing.name.lower() for ing in recipe.ingredients}
        return recipe_ingredients.issubset(self.available_ingredients)


# Ejemplo 3: Composición de Especificaciones para Recetas
def ejemplo_composicion():
    """Ejemplo de cómo componer especificaciones de recetas"""
    
    # Recetas rápidas y fáciles
    quick_and_easy = (
        PreparationTimeSpec(30)
        .and_(DifficultySpec(DifficultyLevel.EASY))
    )
    
    # Recetas vegetarianas bajas en calorías
    healthy_vegetarian = (
        DietTypeSpec(DietType.VEGETARIAN)
        .and_(CaloriesRangeSpec(0, 500))
    )
    
    # Recetas para cena sin gluten
    gluten_free_dinner = (
        MealTypeSpec(MealType.DINNER)
        .and_(DietTypeSpec(DietType.GLUTEN_FREE))
    )
    
    return quick_and_easy, healthy_vegetarian, gluten_free_dinner

