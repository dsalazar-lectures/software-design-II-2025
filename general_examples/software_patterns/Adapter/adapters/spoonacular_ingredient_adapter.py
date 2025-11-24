from interfaces.ingredient_provider import IngredientProvider
from models.ingredient import Ingredient

class SpoonacularIngredientAdapter(IngredientProvider):
    def __init__(self, api_service):
        self.api_service = api_service

    def get_ingredient(self, name: str) -> Ingredient:
        data = self.api_service.search_ingredient(name)
        results = data.get("results", [])

        if not results:
            raise ValueError(f"No se encontró el ingrediente '{name}'")

        first = results[0]
        return Ingredient(
            name=first.get("name"),
            quantity=1,
            unit="unit"
        )
