from abc import ABC, abstractmethod

class IngredientProvider(ABC):
    @abstractmethod
    def get_ingredient(self, ingredient_id: str):
        pass