from services.external_ingredient_api import ExternalIngredientAPI
from services.spoonacular_ingredient_api import SpoonacularIngredientAPI
from adapters.external_ingredient_adapter import ExternalIngredientAdapter
from adapters.spoonacular_ingredient_adapter import SpoonacularIngredientAdapter
from client.ingredient_manager import IngredientManager

def main():

    use_spoonacular = True

    if use_spoonacular:
        print("Usando API Spoonacular")
        service = SpoonacularIngredientAPI(api_key = "ede68984f0a740e9b57412e44d62d162")
        adapter = SpoonacularIngredientAdapter(service)
    else:
        print("Usando API externa genérica")
        service = ExternalIngredientAPI()
        adapter = ExternalIngredientAdapter(service)

    # Cliente que usa la interfaz, no la API externa directamente
    client = IngredientManager([adapter])

    # Procesar un ingrediente (flujo completo)
    client.process_ingredient("tomato")

if __name__ == "__main__":
    main()