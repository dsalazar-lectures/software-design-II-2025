from recipe_dao import RecipeDAO, Recipe

class RecipeDAOImpl(RecipeDAO):
    def __init__(self):
        self._data = []
        self._next_id: int = 1

    # Crear
    def create(self, name, ingredients, author):
        recipe = Recipe(id=self._next_id, name=name.strip(), ingredients=list(ingredients), author=author.strip())
        self._data.append(recipe)
        self._next_id += 1
        return recipe

    # Leer
    def get_all(self):
        return list(self._data)

    def get_by_id(self, recipe_id):
        return next((r for r in self._data if r.id == recipe_id), None)

    # Actualizar
    def update(self, recipe_id, name=None, ingredients=None):
        recipe = self.get_by_id(recipe_id)
        if recipe is None:
            return None
        if name is not None:
            recipe.name = name.strip()
        if ingredients is not None:
            recipe.ingredients = list(ingredients)
        return recipe

    # Eliminar
    def delete(self, recipe_id):
        recipe = self.get_by_id(recipe_id)
        if recipe is None:
            return False
        self._data.remove(recipe)
        return True
