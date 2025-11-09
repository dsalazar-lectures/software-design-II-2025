from abc import ABC, abstractmethod
from typing import List, Set
from enum import Enum

# Ejemplo 1: Estructura Base del Patrón Specification
class Specification(ABC):
    """Interfaz base para especificaciones"""
    
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass
    
    def and_(self, other):
        return AndSpecification(self, other)
    
    def or_(self, other):
        return OrSpecification(self, other)
    
    def not_(self):
        return NotSpecification(self)


class AndSpecification(Specification):
    """Combina dos especificaciones con AND lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)


class OrSpecification(Specification):
    """Combina dos especificaciones con OR lógico"""
    
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)


class NotSpecification(Specification):
    """Niega una especificación"""
    
    def __init__(self, spec: Specification):
        self.spec = spec
    
    def is_satisfied_by(self, candidate):
        return not self.spec.is_satisfied_by(candidate)


# Modelos del Dominio: Ingrediente, Receta, Menú
class DietType(Enum):
    """Tipos de dietas"""
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten_free"
    KETO = "keto"
    PALEO = "paleo"
    OMNIVORE = "omnivore"


class DifficultyLevel(Enum):
    """Niveles de dificultad"""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class MealType(Enum):
    """Tipos de comidas"""
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
    DESSERT = "dessert"


class Ingredient:
    """Representa un ingrediente"""
    
    def __init__(self, name: str, quantity: float, unit: str, calories: int = 0):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories = calories
    
    def __repr__(self):
        return f"{self.quantity} {self.unit} de {self.name}"


class Recipe:
    """Representa una receta de cocina"""
    
    def __init__(self, name: str, ingredients: List[Ingredient], 
                 preparation_time: int, difficulty: DifficultyLevel,
                 servings: int, diet_types: List[DietType],
                 meal_types: List[MealType], calories: int = 0):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time  # en minutos
        self.difficulty = difficulty
        self.servings = servings
        self.diet_types = diet_types
        self.meal_types = meal_types
        self.calories = calories if calories > 0 else sum(ing.calories for ing in ingredients)
    
    def __repr__(self):
        return f"Recipe({self.name}, {self.preparation_time}min, {self.difficulty.value})"


class Menu:
    """Representa un menú compuesto por varias recetas"""
    
    def __init__(self, name: str, recipes: List[Recipe]):
        self.name = name
        self.recipes = recipes
    
    @property
    def total_calories(self):
        return sum(recipe.calories for recipe in self.recipes)
    
    @property
    def total_preparation_time(self):
        return sum(recipe.preparation_time for recipe in self.recipes)
    
    def __repr__(self):
        return f"Menu({self.name}, {len(self.recipes)} recetas)"


# Ejemplo 2: Especificaciones para Recetas
class HasIngredientSpec(Specification):
    """Verifica si la receta contiene un ingrediente específico"""
    
    def __init__(self, ingredient_name: str):
        self.ingredient_name = ingredient_name.lower()
    
    def is_satisfied_by(self, recipe):
        return any(ing.name.lower() == self.ingredient_name for ing in recipe.ingredients)


class HasAllIngredientsSpec(Specification):
    """Verifica si la receta contiene todos los ingredientes especificados"""
    
    def __init__(self, ingredient_names: List[str]):
        self.ingredient_names = [name.lower() for name in ingredient_names]
    
    def is_satisfied_by(self, recipe):
        recipe_ingredients = [ing.name.lower() for ing in recipe.ingredients]
        return all(name in recipe_ingredients for name in self.ingredient_names)


class AvoidIngredientSpec(Specification):
    """Verifica que la receta NO contenga un ingrediente específico (alergias)"""
    
    def __init__(self, ingredient_name: str):
        self.ingredient_name = ingredient_name.lower()
    
    def is_satisfied_by(self, recipe):
        return not any(ing.name.lower() == self.ingredient_name for ing in recipe.ingredients)


class PreparationTimeSpec(Specification):
    """Verifica si el tiempo de preparación está dentro de un límite"""
    
    def __init__(self, max_minutes: int):
        self.max_minutes = max_minutes
    
    def is_satisfied_by(self, recipe):
        return recipe.preparation_time <= self.max_minutes


class DifficultySpec(Specification):
    """Verifica el nivel de dificultad de la receta"""
    
    def __init__(self, difficulty: DifficultyLevel):
        self.difficulty = difficulty
    
    def is_satisfied_by(self, recipe):
        return recipe.difficulty == self.difficulty


class CaloriesRangeSpec(Specification):
    """Verifica si las calorías están dentro de un rango"""
    
    def __init__(self, min_calories: int, max_calories: int):
        self.min_calories = min_calories
        self.max_calories = max_calories
    
    def is_satisfied_by(self, recipe):
        return self.min_calories <= recipe.calories <= self.max_calories


class DietTypeSpec(Specification):
    """Verifica si la receta es compatible con un tipo de dieta"""
    
    def __init__(self, diet_type: DietType):
        self.diet_type = diet_type
    
    def is_satisfied_by(self, recipe):
        return self.diet_type in recipe.diet_types


class MealTypeSpec(Specification):
    """Verifica el tipo de comida (desayuno, almuerzo, cena, etc.)"""
    
    def __init__(self, meal_type: MealType):
        self.meal_type = meal_type
    
    def is_satisfied_by(self, recipe):
        return self.meal_type in recipe.meal_types


class ServingsSpec(Specification):
    """Verifica si la receta sirve para un número específico de personas"""
    
    def __init__(self, min_servings: int, max_servings: int):
        self.min_servings = min_servings
        self.max_servings = max_servings
    
    def is_satisfied_by(self, recipe):
        return self.min_servings <= recipe.servings <= self.max_servings


class AvailableIngredientsSpec(Specification):
    """Verifica si todos los ingredientes de la receta están disponibles en la despensa"""
    
    def __init__(self, available_ingredients: Set[str]):
        self.available_ingredients = {ing.lower() for ing in available_ingredients}
    
    def is_satisfied_by(self, recipe):
        recipe_ingredients = {ing.name.lower() for ing in recipe.ingredients}
        return recipe_ingredients.issubset(self.available_ingredients)


# Ejemplo 3: Composición de Especificaciones para Recetas
def ejemplo_composicion():
    """Ejemplo de cómo componer especificaciones de recetas"""
    
    # Recetas rápidas y fáciles
    quick_and_easy = (
        PreparationTimeSpec(30)
        .and_(DifficultySpec(DifficultyLevel.EASY))
    )
    
    # Recetas vegetarianas bajas en calorías
    healthy_vegetarian = (
        DietTypeSpec(DietType.VEGETARIAN)
        .and_(CaloriesRangeSpec(0, 500))
    )
    
    # Recetas para cena sin gluten
    gluten_free_dinner = (
        MealTypeSpec(MealType.DINNER)
        .and_(DietTypeSpec(DietType.GLUTEN_FREE))
    )
    
    return quick_and_easy, healthy_vegetarian, gluten_free_dinner


# Ejemplo 4: Especificaciones Compuestas de Alto Nivel
class QuickMealSpec(Specification):
    """Comida rápida: fácil de preparar y en poco tiempo"""
    
    def __init__(self):
        self.spec = (
            PreparationTimeSpec(30)
            .and_(DifficultySpec(DifficultyLevel.EASY))
        )
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class HealthyDietSpec(Specification):
    """Receta saludable: baja en calorías y rica en nutrientes"""
    
    def __init__(self):
        self.spec = CaloriesRangeSpec(0, 600)
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class FamilyFriendlySpec(Specification):
    """Receta para familia: sirve para 4-6 personas, fácil de hacer"""
    
    def __init__(self):
        self.spec = (
            ServingsSpec(4, 6)
            .and_(DifficultySpec(DifficultyLevel.EASY).or_(DifficultySpec(DifficultyLevel.MEDIUM)))
        )
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


class GourmetSpec(Specification):
    """Receta gourmet: alta dificultad, para ocasiones especiales"""
    
    def __init__(self):
        self.spec = DifficultySpec(DifficultyLevel.HARD)
    
    def is_satisfied_by(self, recipe):
        return self.spec.is_satisfied_by(recipe)


# Ejemplo 5: Repository Pattern para Recetas
class RecipeRepository:
    """Repositorio de recetas que soporta especificaciones"""
    
    def __init__(self, recipes: List[Recipe]):
        self._recipes = recipes
    
    def find(self, specification: Specification) -> List[Recipe]:
        """Encuentra recetas que cumplan la especificación"""
        return [r for r in self._recipes if specification.is_satisfied_by(r)]
    
    def find_one(self, specification: Specification) -> Recipe:
        """Encuentra la primera receta que cumpla la especificación"""
        for recipe in self._recipes:
            if specification.is_satisfied_by(recipe):
                return recipe
        return None
    
    def count(self, specification: Specification) -> int:
        """Cuenta recetas que cumplan la especificación"""
        return len(self.find(specification))


# Ejemplo 6: Factory de Especificaciones para Recetas
class RecipeSpecs:
    """Factory para especificaciones comunes de recetas"""
    
    @staticmethod
    def quick_meal():
        """Comidas rápidas (menos de 30 minutos)"""
        return QuickMealSpec()
    
    @staticmethod
    def healthy():
        """Recetas saludables (menos de 600 calorías)"""
        return HealthyDietSpec()
    
    @staticmethod
    def vegetarian():
        """Recetas vegetarianas"""
        return DietTypeSpec(DietType.VEGETARIAN)
    
    @staticmethod
    def vegan():
        """Recetas veganas"""
        return DietTypeSpec(DietType.VEGAN)
    
    @staticmethod
    def gluten_free():
        """Recetas sin gluten"""
        return DietTypeSpec(DietType.GLUTEN_FREE)
    
    @staticmethod
    def breakfast():
        """Recetas para desayuno"""
        return MealTypeSpec(MealType.BREAKFAST)
    
    @staticmethod
    def dinner():
        """Recetas para cena"""
        return MealTypeSpec(MealType.DINNER)
    
    @staticmethod
    def family_friendly():
        """Recetas familiares"""
        return FamilyFriendlySpec()
    
    @staticmethod
    def with_ingredients(available: Set[str]):
        """Recetas con ingredientes disponibles"""
        return AvailableIngredientsSpec(available)
    
    @staticmethod
    def without_allergen(allergen: str):
        """Recetas sin un alérgeno específico"""
        return AvoidIngredientSpec(allergen)


# Especificaciones para Menús
class BalancedMenuSpec(Specification):
    """Verifica si un menú es balanceado (tiene desayuno, almuerzo y cena)"""
    
    def is_satisfied_by(self, menu):
        meal_types = set()
        for recipe in menu.recipes:
            meal_types.update(recipe.meal_types)
        
        return (MealType.BREAKFAST in meal_types and 
                MealType.LUNCH in meal_types and 
                MealType.DINNER in meal_types)


class TotalCaloriesSpec(Specification):
    """Verifica si las calorías totales del menú están en un rango"""
    
    def __init__(self, min_calories: int, max_calories: int):
        self.min_calories = min_calories
        self.max_calories = max_calories
    
    def is_satisfied_by(self, menu):
        return self.min_calories <= menu.total_calories <= self.max_calories


class TimeEfficientMenuSpec(Specification):
    """Verifica si el menú completo se puede preparar en un tiempo razonable"""
    
    def __init__(self, max_total_minutes: int):
        self.max_total_minutes = max_total_minutes
    
    def is_satisfied_by(self, menu):
        return menu.total_preparation_time <= self.max_total_minutes


# Ejemplo de Uso Completo
def main():
    """Ejemplo completo del patrón Specification con Recetas y Menús"""

    print("PATRÓN SPECIFICATION - SISTEMA DE RECETAS Y MENÚS")
    
    # Crear ingredientes
    huevos = Ingredient("huevos", 2, "unidades", 140)
    leche = Ingredient("leche", 100, "ml", 60)
    harina = Ingredient("harina", 200, "g", 280)
    azucar = Ingredient("azúcar", 50, "g", 200)
    mantequilla = Ingredient("mantequilla", 30, "g", 215)
    pollo = Ingredient("pollo", 200, "g", 220)
    arroz = Ingredient("arroz", 150, "g", 195)
    verduras = Ingredient("verduras", 200, "g", 80)
    tomate = Ingredient("tomate", 100, "g", 18)
    lechuga = Ingredient("lechuga", 50, "g", 8)
    queso = Ingredient("queso", 50, "g", 200)
    
    # Crear recetas
    recetas = [
        Recipe(
            "Panqueques",
            [huevos, leche, harina, azucar, mantequilla],
            20,
            DifficultyLevel.EASY,
            4,
            [DietType.VEGETARIAN],
            [MealType.BREAKFAST, MealType.DESSERT],
            895
        ),
        Recipe(
            "Pollo con Arroz",
            [pollo, arroz, verduras],
            45,
            DifficultyLevel.MEDIUM,
            4,
            [DietType.OMNIVORE, DietType.GLUTEN_FREE],
            [MealType.LUNCH, MealType.DINNER],
            495
        ),
        Recipe(
            "Ensalada César",
            [lechuga, queso, huevos],
            15,
            DifficultyLevel.EASY,
            2,
            [DietType.VEGETARIAN, DietType.KETO],
            [MealType.LUNCH, MealType.DINNER],
            348
        ),
        Recipe(
            "Omelette de Verduras",
            [huevos, verduras, queso],
            15,
            DifficultyLevel.EASY,
            2,
            [DietType.VEGETARIAN, DietType.KETO, DietType.GLUTEN_FREE],
            [MealType.BREAKFAST, MealType.LUNCH],
            420
        ),
        Recipe(
            "Arroz con Verduras",
            [arroz, verduras, tomate],
            30,
            DifficultyLevel.EASY,
            4,
            [DietType.VEGAN, DietType.VEGETARIAN, DietType.GLUTEN_FREE],
            [MealType.LUNCH, MealType.DINNER],
            293
        ),
    ]
    
    # Crear repositorio
    repo = RecipeRepository(recetas)
    
    # Ejemplo 1: Recetas rápidas (menos de 30 minutos)
    print("\n\nRECETAS RÁPIDAS (< 30 minutos):")
    print("-" * 70)
    recetas_rapidas = repo.find(RecipeSpecs.quick_meal())
    for r in recetas_rapidas:
        print(f"{r.name} - {r.preparation_time} minutos")
    
    # Ejemplo 2: Recetas vegetarianas
    print("\n\nRECETAS VEGETARIANAS:")
    print("-" * 70)
    recetas_vegetarianas = repo.find(RecipeSpecs.vegetarian())
    for r in recetas_vegetarianas:
        print(f"{r.name} - {r.calories} calorías")

    # Ejemplo 3: Recetas para desayuno, rápidas y fáciles
    print("\n\nDESAYUNOS RÁPIDOS Y FÁCILES:")
    print("-" * 70)
    desayunos_faciles = repo.find(
        RecipeSpecs.breakfast()
        .and_(PreparationTimeSpec(20))
        .and_(DifficultySpec(DifficultyLevel.EASY))
    )
    for r in desayunos_faciles:
        print(f"{r.name} - {r.preparation_time} min, {r.difficulty.value}")
    
    # Ejemplo 4: Recetas saludables para cena
    print("\n\nCENAS SALUDABLES (< 500 calorías):")
    print("-" * 70)
    cenas_saludables = repo.find(
        RecipeSpecs.dinner()
        .and_(CaloriesRangeSpec(0, 500))
    )
    for r in cenas_saludables:
        print(f"{r.name} - {r.calories} calorías")
    
    # Ejemplo 5: Recetas sin lácteos (evitar alergia)
    print("\n\nRECETAS SIN LÁCTEOS:")
    print("-" * 70)
    sin_lacteos = repo.find(
        RecipeSpecs.without_allergen("leche")
        .and_(RecipeSpecs.without_allergen("queso"))
        .and_(RecipeSpecs.without_allergen("mantequilla"))
    )
    for r in sin_lacteos:
        print(f"{r.name}")
    
    # Ejemplo 6: Recetas con ingredientes disponibles
    print("\n\nRECETAS CON INGREDIENTES DISPONIBLES:")
    print("-" * 70)
    despensa = {"huevos", "verduras", "queso", "arroz", "tomate"}
    print(f"Ingredientes en despensa: {', '.join(despensa)}")
    print()
    con_ingredientes = repo.find(RecipeSpecs.with_ingredients(despensa))
    for r in con_ingredientes:
        ingredientes = ", ".join([ing.name for ing in r.ingredients])
        print(f"{r.name}")
        print(f"    Ingredientes: {ingredientes}")
    
    # Ejemplo 7: Crear y validar un menú
    print("\n\nVALIDACIÓN DE MENÚ DIARIO:")
    print("-" * 70)
    menu_dia = Menu("Menú del Día", [
        recetas[3],  # Omelette (desayuno)
        recetas[2],  # Ensalada (almuerzo)
        recetas[4],  # Arroz con verduras (cena)
    ])
    
    print(f"Menú: {menu_dia.name}")
    print(f"Recetas incluidas:")
    for r in menu_dia.recipes:
        tipos = ", ".join([mt.value for mt in r.meal_types])
        print(f"- {r.name} ({tipos})")
    print(f"\nCalorías totales: {menu_dia.total_calories} cal")
    print(f"Tiempo total de preparación: {menu_dia.total_preparation_time} min")
    
    # Validar menú
    menu_balanceado = BalancedMenuSpec()
    menu_calorias = TotalCaloriesSpec(800, 2000)
    menu_eficiente = TimeEfficientMenuSpec(120)
    
    print(f"\n ¿Menú balanceado? {menu_balanceado.is_satisfied_by(menu_dia)}")
    print(f"¿Calorías adecuadas? {menu_calorias.is_satisfied_by(menu_dia)}")
    print(f"¿Tiempo eficiente? {menu_eficiente.is_satisfied_by(menu_dia)}")
    
    # Ejemplo 8: Búsqueda compleja
    print("\n\nBÚSQUEDA COMPLEJA - Recetas para familia vegetariana:")
    print("-" * 70)
    recetas_familia = repo.find(
        RecipeSpecs.vegetarian()
        .and_(ServingsSpec(4, 6))
        .and_(PreparationTimeSpec(45))
        .and_(CaloriesRangeSpec(0, 600))
    )
    for r in recetas_familia:
        print(f"{r.name}")
        print(f"Porciones: {r.servings}, Tiempo: {r.preparation_time} min")
        print(f"Calorías: {r.calories}, Dificultad: {r.difficulty.value}")


if __name__ == "__main__":
    main()
