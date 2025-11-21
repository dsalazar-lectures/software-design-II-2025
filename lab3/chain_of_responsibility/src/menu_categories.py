from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, List

# Small example of menus
MENU_DATA: Dict[str, List[str]] = {
  "breakfast": ["Cereal with Milk", "Oatmeal with Fruit", "Pancakes with Syrup", "Fruit Bowl"],
  "snack":     ["Cookies", "Cereal Bar", "Popcorn", "Donut"],
  "lunch":     ["Salad", "Sandwich", "Soup and Bread", "Fish and Chips"],
  "dinner":    ["Spaghetti with Meatballs", "Roast Chicken with vegetables", "Steak with Baked Potato"],
  "dessert":   ["Cake", "Ice Cream", "Pie", "Cheesecake", "Fruit Tart"],
  "drink":     ["Orange Juice", "Black Coffee", "Green Tea", "Iced Latte", "Hot Chocolate"]
}

class Handler(ABC):
  @abstractmethod
  def set_next(self, handler: "Handler") -> "Handler":
    pass
  @abstractmethod
  def handle(self, request) -> Optional[str]:
    pass

# Base of handlers
class BaseHandler(Handler, ABC):
  def __init__(self, nxt: Optional["Handler"]=None):
    self._next: Optional[Handler] = nxt

  def set_next(self, handler: "Handler") -> "Handler":
    self._next = handler
    return handler

  def handle(self, request: Any) -> Optional[str]:
    result = self._try(request)
    if result is not None:
      return result
    return self._next.handle(request) if self._next else None

  @abstractmethod
  def _try(self, request: Any) -> Optional[str]:
    pass

# Base of categories handlers
class CategoryHandler(BaseHandler, ABC):
  @property
  @abstractmethod
  def category(self) -> str:
    pass

  def _try(self, request: Any) -> Optional[str]:
    if isinstance(request, str) and request.lower() == self.category:
      items = MENU_DATA.get(self.category, [])
      return f"Here are some menus for {self.category}: {items}"
    return None

# Concrete handlers of menus
class BreakfastHandler(CategoryHandler):
  @property
  def category(self) -> str: return "breakfast"

class SnackHandler(CategoryHandler):
  @property
  def category(self) -> str: return "snack"

class LunchHandler(CategoryHandler):
  @property
  def category(self) -> str: return "lunch"

class DinnerHandler(CategoryHandler):
  @property
  def category(self) -> str: return "dinner"

class DessertHandler(CategoryHandler):
  @property
  def category(self) -> str: return "dessert"

class DrinkHandler(CategoryHandler):
  @property
  def category(self) -> str: return "drink"
