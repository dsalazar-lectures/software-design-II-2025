from typing import List, Set
from specification_base import Specification
from models import DietType, DifficultyLevel, MealType


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


class QuickMealSpec(Specification):
    """Comida rápida: fácil de preparar y en poco tiempo"""
    
    def __init__(self):
        self.spec = (
            PreparationTimeSpec(30)
            .and_(DifficultySpec(DifficultyLevel.EASY))
        )
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class HealthyDietSpec(Specification):
    """Receta saludable: baja en calorías y rica en nutrientes"""
    
    def __init__(self):
        self.spec = CaloriesRangeSpec(0, 600)
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class FamilyFriendlySpec(Specification):
    """Receta para familia: sirve para 4-6 personas, fácil de hacer"""
    
    def __init__(self):
        self.spec = (
            ServingsSpec(4, 6)
            .and_(DifficultySpec(DifficultyLevel.EASY).or_(DifficultySpec(DifficultyLevel.MEDIUM)))
        )
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class GourmetSpec(Specification):
    """Receta gourmet: alta dificultad, para ocasiones especiales"""
    
    def __init__(self):
        self.spec = DifficultySpec(DifficultyLevel.HARD)
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)
