from typing import Set
from recipe_specifications import (
    QuickMealSpec,
    HealthyDietSpec,
    DietTypeSpec,
    MealTypeSpec,
    FamilyFriendlySpec,
    AvailableIngredientsSpec,
    AvoidIngredientSpec
)
from models import DietType, MealType


class RecipeSpecs:
    """Factory para especificaciones comunes de recetas"""
    
    @staticmethod
    def quick_meal():
        """Comidas rápidas (menos de 30 minutos)"""
        return QuickMealSpec()
    
    @staticmethod
    def healthy():
        """Recetas saludables (menos de 600 calorías)"""
        return HealthyDietSpec()
    
    @staticmethod
    def vegetarian():
        """Recetas vegetarianas"""
        return DietTypeSpec(DietType.VEGETARIAN)
    
    @staticmethod
    def vegan():
        """Recetas veganas"""
        return DietTypeSpec(DietType.VEGAN)
    
    @staticmethod
    def gluten_free():
        """Recetas sin gluten"""
        return DietTypeSpec(DietType.GLUTEN_FREE)
    
    @staticmethod
    def breakfast():
        """Recetas para desayuno"""
        return MealTypeSpec(MealType.BREAKFAST)
    
    @staticmethod
    def dinner():
        """Recetas para cena"""
        return MealTypeSpec(MealType.DINNER)
    
    @staticmethod
    def family_friendly():
        """Recetas familiares"""
        return FamilyFriendlySpec()
    
    @staticmethod
    def with_ingredients(available: Set[str]):
        """Recetas con ingredientes disponibles"""
        return AvailableIngredientsSpec(available)
    
    @staticmethod
    def without_allergen(allergen: str):
        """Recetas sin un alérgeno específico"""
        return AvoidIngredientSpec(allergen)
