from Recipe.IGetRecipe import IGetRecipe
from Profile.IUserProfile import IUserProfile
from Recipe.GetRecipe import GetRecipe
from Profile.UserProfile import UserProfile


class RecipeAPI:
    """
    Fachada que simplifica el acceso a los subsistemas de recetas y usuarios.
    Proporciona una interfaz unificada para operaciones complejas del recetario.
    """

    def __init__(self):
        # Interfaces a los subsistemas
        self._recipes: IGetRecipe = GetRecipe()
        self._users: IUserProfile = UserProfile()

    def get_recipe_for_user(self, user_id, recipe_id):
        """Obtiene toda la información de una receta adaptada al usuario"""
        user_prefs = self._users.get_user_preferences(user_id)
        recipe_details = self._recipes.get_recipe_details(recipe_id)
        ingredients = self._recipes.get_ingredients(recipe_id)

        # Filtrar ingredientes según preferencias del usuario
        filtered_ingredients = self._filter_ingredients(
            ingredients, user_prefs)

        return {
            "recipe": recipe_details,
            "ingredients": filtered_ingredients,
            "adapted_for": user_prefs
        }

    def _filter_ingredients(self, ingredients, user_prefs):
        # Lógica simplificada de filtrado
        if "vegetariano" in user_prefs.get("diet", ""):
            return [ing for ing in ingredients if ing != "panceta"]
        return ingredients
