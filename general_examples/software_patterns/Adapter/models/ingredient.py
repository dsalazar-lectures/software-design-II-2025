class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"Ingredient(name={self.name}, quantity={self.quantity}, unit={self.unit})"
