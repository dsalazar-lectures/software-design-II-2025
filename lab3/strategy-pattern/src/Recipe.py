class Recipe:
    def __init__(self, name, category, ingredients, instructions, rating):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        self.rating = float(rating) # cast to float
    
    def __str__(self):
        return f"{self.name} ({self.category}) Rating: {self.rating}"
    
    def showFullRecipe(self):
        return f"\nReceta: {self.name}\nCategoría: {self.category}\nRating: {self.rating}\nIngredientes:\n{self.ingredients}\nInstrucciones:\n{self.instructions}\n"
