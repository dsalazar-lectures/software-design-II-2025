
from menu_categories import (
  Handler, BreakfastHandler, SnackHandler, LunchHandler,
  DinnerHandler, DessertHandler, DrinkHandler
)
from typing import List

def demo_generate_menu(handler: Handler, categories : List) -> None:
  for category in categories:
    print(f"\nClient: Please generate {category!r}")
    result = handler.handle(category)
    if result:
      print(" ", result, end="")
    else:
      print(f"  No handler processed {category!r}.", end="")

if __name__ == "__main__":
  categories = ["breakfast", "snack", "lunch", "dinner", "dessert", "drink"]

  root = BreakfastHandler()
  root.set_next(SnackHandler()) \
      .set_next(LunchHandler()) \
      .set_next(DinnerHandler()) \
      .set_next(DessertHandler()) \
      .set_next(DrinkHandler()) \
      # .set_next(MainMenuHandler())

  # All categories
  print("Chain: Breakfast > Snack > Lunch > Dinner > Dessert > Drink")
  demo_generate_menu(root, categories)
  print("\n")

  # Subcategories
  sub = LunchHandler()
  sub.set_next(DessertHandler())
  print("Subchain: Lunch > Dessert")
  demo_generate_menu(sub, categories)
