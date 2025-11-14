from interfaces.ingredient_provider import IngredientProvider

class IngredientManager:
    def __init__(self, provider: IngredientProvider):
        self.provider = provider

    def process_ingredient(self, ingredient_id: str):
        for provider in self.provider:
            ingredient = provider.get_ingredient(ingredient_id)
            if ingredient:
                self.save_ingredient(ingredient)
                break
        else:
            print(f"Ingredient with ID {ingredient_id} not found in any provider.")

    def save_ingredient(self, ingredient):
        print(f" Saved ingredient: {ingredient}")
