from csvLoader import loadRecipes
from RecipeFilter import RecipeFilter
from FilterByRating import FilterByRating
from FilterByIngredient import FilterByIngredient
from FilterByCategory import FilterByCategory

if __name__ == "__main__":

    recipes = loadRecipes('ExampleRecipes.csv')
    
    print("**Todas las recipes cargadas**")
    for recipe in recipes:
        print(recipe.showFullRecipe())
    
    # creación del contexto
    filter = RecipeFilter()
    
    # primera estrategia - rating
    print("**Filtrar rating**")
    filter.setStrategy(FilterByRating())
    resultado = filter.applyFilter(recipes, 8)
    for recipe in resultado:
        print(recipe)
    print()
    
    # segunda estrategia - ingrediente
    print("**Filtrar ingrediente**")
    filter.setStrategy(FilterByIngredient())
    resultado = filter.applyFilter(recipes, "huevo")
    for recipe in resultado:
        print(recipe)
    print()
    
    # tercera estrategia - categoría
    print("**Filtrar categoría**")
    filter.setStrategy(FilterByCategory())
    resultado = filter.applyFilter(recipes, "postre")
    for recipe in resultado:
        print(recipe)
    print()
    
    # cambios en el parámetro de la estrategia durante la ejecución
    print("*Cambio*")
    print("**Filtrando por una categoría distinta**")
    filter.setStrategy(FilterByCategory())
    resultado = filter.applyFilter(recipes, "cena")
    for recipe in resultado:
        print(recipe)
