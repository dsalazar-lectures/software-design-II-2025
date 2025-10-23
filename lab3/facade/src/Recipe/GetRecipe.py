from Recipe.IGetRecipe import IGetRecipe


class GetRecipe(IGetRecipe):
    # Implementación simulada de acceso a recetas
    def get_recipe_details(self, recipe_id):
        print(f"Obteniendo detalles de receta {recipe_id}")
        return {"id": recipe_id, "name": "Pasta Carbonara"}

    def get_ingredients(self, recipe_id):
        print(f"Obteniendo ingredientes para receta {recipe_id}")
        return ["pasta", "huevo", "panceta", "queso"]

    def get_cooking_steps(self, recipe_id):
        print(f"Obteniendo pasos de cocción para receta {recipe_id}")
        return ["Cocer pasta", "Preparar salsa", "Mezclar"]
