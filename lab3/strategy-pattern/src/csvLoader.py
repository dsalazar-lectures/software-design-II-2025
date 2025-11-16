import csv
import os
from Recipe import Recipe

def loadRecipes(csvFile: str):
    # obtener directorio
    currentDir = os.path.dirname(os.path.abspath(__file__))
    csvPath = os.path.join(currentDir, 'data', csvFile)
    
    recipes = []
    with open(csvPath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipes.append(Recipe(
                row['name'].strip(),
                row['category'].strip(),
                row['ingredients'].strip(),
                row['instructions'].strip(),
                row['rating'].strip()
            ))
    return recipes