"""
Repository Pattern.
Run:
    python lab3/repository/src/main.py
"""

from recipe import Recipe
from json_recipe_repository import JsonRecipeRepository


def main():
    # 1) Initialize repository (Replace the repository class to switch repositories)
    repo = JsonRecipeRepository()

    # 2) Add recipes
    print("\nAdding recipes...")
    repo.add(Recipe(1, "Pasta Alfredo", ["pasta", "cream", "parmesan"], 25))
    repo.add(Recipe(2, "Caesar Salad", ["lettuce", "chicken", "croutons"], 15))

    # 3) Display all recipes
    print("\nAll recipes:")
    for r in repo.get_all():
        print(" -", r)

    # 4) Retrieve one by ID
    print("\nFetching recipe with ID=1:")
    recipe = repo.get_by_id(1)

    # 5) Delete one recipe
    print("\nDeleting recipe with ID=2...")
    success = repo.delete(2)
    print("Deleted successfully")

    # 6) Display remaining recipes
    print("\nRemaining recipes:")
    for r in repo.get_all():
        print(" -", r)


if __name__ == "__main__":
    main()
