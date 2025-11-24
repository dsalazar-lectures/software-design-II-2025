import requests

class SpoonacularIngredientAPI:
    BASE_URL = "https://api.spoonacular.com"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search_ingredient(self, name: str, number: int = 1):
        url = f"{self.BASE_URL}/food/ingredients/search"
        params = {
            "apiKey": self.api_key,
            "query": name,
            "number": number
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
