"""
Domain entity: Recipe
Represents a single recipe in the system.
"""

class Recipe:
    def __init__(self, id: int, name: str, ingredients: list[str], duration: int):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.duration} min) | Ingredients: {', '.join(self.ingredients)}"
