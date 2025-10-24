import time


class IngredientSource:
    def __init__(self):
        # mock data
        self._data = {
            "butter": "Butter",
            "milk": "Whole Milk",
            "egg": "Egg",
            "sugar": "White Sugar",
            "flour": "Wheat Flour",
        }

    def get(self, name: str):
        # simulate a big cost call
        time.sleep(1)
        return self._data.get(name.lower())
