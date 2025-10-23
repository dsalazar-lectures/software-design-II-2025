"""
Facade Pattern.
Run:
    python3 lab3/facade/src/main.py
"""

from RecipeAPI import RecipeAPI


def main():
    api = RecipeAPI()

    # Cliente solo requiere llamar a un método simple (la fachada)
    result = api.get_recipe_for_user("user123", "recipe456")
    print(f"Receta adaptada: {result}")


if __name__ == "__main__":
    main()
