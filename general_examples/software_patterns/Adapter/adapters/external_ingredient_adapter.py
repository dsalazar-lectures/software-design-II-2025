from interfaces.ingredient_provider import IngredientProvider
from models.ingredient import Ingredient

class ExternalIngredientAdapter(IngredientProvider):
    def __init__(self, external_api):
        self.external_api = external_api

    def get_ingredient(self, ingredient_id: str) -> Ingredient:
        data = self.external_api.fetch_ingredient_data(ingredient_id)
        return Ingredient(
            name=data["ingredientName"],
            quantity=data["amount"],
            unit=data["measurement"]
        )
