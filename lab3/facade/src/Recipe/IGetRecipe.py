from abc import ABC, abstractmethod


class IGetRecipe(ABC):
    @abstractmethod
    def get_recipe_details(self, recipe_id):
        pass

    @abstractmethod
    def get_ingredients(self, recipe_id):
        pass

    @abstractmethod
    def get_cooking_steps(self, recipe_id):
        pass
