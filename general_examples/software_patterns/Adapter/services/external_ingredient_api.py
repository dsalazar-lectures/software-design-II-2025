class ExternalIngredientAPI:
    """Simula una API externa con un formato distinto."""
    def fetch_ingredient_data(self, ingredient_id: str):
        return {
            "ingredientName": "Tomato",
            "amount": 2.5,
            "measurement": "kg"
        }
