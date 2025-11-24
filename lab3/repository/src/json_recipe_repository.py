"""
Concrete implementation of RecipeRepository
using JSON file storage as the persistence layer.
"""

import json
from typing import List
from recipe import Recipe


class JsonRecipeRepository():
    """Implements the repository with simple JSON file persistence."""

    def __init__(self, file_path: str = "recipes.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def _save(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    def get_all(self) -> List[Recipe]:
        return [Recipe(**r) for r in self.data]

    def get_by_id(self, recipe_id: int) -> Recipe:
        for r in self.data:
            if r["id"] == recipe_id:
                return Recipe(**r)
        return None

    def add(self, recipe: Recipe) -> None:
        self.data.append(recipe.__dict__)
        self._save()

    def delete(self, recipe_id: int) -> bool:
        for r in self.data:
            if r["id"] == recipe_id:
                self.data.remove(r)
                self._save()
                return True
        return False
