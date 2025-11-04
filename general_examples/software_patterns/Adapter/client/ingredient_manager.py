from interfaces.ingredient_provider import IngredientProvider

class IngredientManager:
    def __init__(self, provider: IngredientProvider):
        self.provider = provider

    def process_ingredient(self, ingredient_id: str):
        ingredient = self.provider.get_ingredient(ingredient_id)
        self.save_ingredient(ingredient)

    def save_ingredient(self, ingredient):
        print(f" Saved ingredient: {ingredient}")
