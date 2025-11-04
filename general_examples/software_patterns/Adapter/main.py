from services.external_ingredient_api import ExternalIngredientAPI
from adapters.external_ingredient_adapter import ExternalIngredientAdapter
from client.ingredient_manager import IngredientManager

def main():
    # Servicio externo incompatible
    external_service = ExternalIngredientAPI()

    # Adaptador que traduce al formato interno
    adapter = ExternalIngredientAdapter(external_service)

    # Cliente que usa la interfaz, no la API externa directamente
    client = IngredientManager(adapter)

    # Procesar un ingrediente (flujo completo)
    client.process_ingredient("123")

if __name__ == "__main__":
    main()