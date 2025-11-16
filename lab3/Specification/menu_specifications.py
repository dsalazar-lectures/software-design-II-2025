from specification_base import Specification
from models import MealType


class BalancedMenuSpec(Specification):
    """Verifica si un menú es balanceado (tiene desayuno, almuerzo y cena)"""
    
    def is_satisfied_by(self, menu):
        meal_types = set()
        for recipe in menu.recipes:
            meal_types.update(recipe.meal_types)
        
        return (MealType.BREAKFAST in meal_types and 
                MealType.LUNCH in meal_types and 
                MealType.DINNER in meal_types)


class TotalCaloriesSpec(Specification):
    """Verifica si las calorías totales del menú están en un rango"""
    
    def __init__(self, min_calories: int, max_calories: int):
        self.min_calories = min_calories
        self.max_calories = max_calories
    
    def is_satisfied_by(self, menu):
        return self.min_calories <= menu.total_calories <= self.max_calories


class TimeEfficientMenuSpec(Specification):
    """Verifica si el menú completo se puede preparar en un tiempo razonable"""
    
    def __init__(self, max_total_minutes: int):
        self.max_total_minutes = max_total_minutes
    
    def is_satisfied_by(self, menu):
        return menu.total_preparation_time <= self.max_total_minutes
