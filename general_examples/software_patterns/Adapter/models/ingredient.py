class Ingredient:
    def __init__(self, name: str, quantity: float = 0.0, unit: str = "", **extra):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.extra = extra

    def __repr__(self):
        return f"Ingredient(name={self.name}, quantity={self.quantity}, unit={self.unit})"
