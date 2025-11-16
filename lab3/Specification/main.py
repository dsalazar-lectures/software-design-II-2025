from models import Ingredient, Recipe, Menu, DietType, DifficultyLevel, MealType
from repository import RecipeRepository
from recipe_specs_factory import RecipeSpecs
from recipe_specifications import PreparationTimeSpec, DifficultySpec, CaloriesRangeSpec, ServingsSpec
from menu_specifications import BalancedMenuSpec, TotalCaloriesSpec, TimeEfficientMenuSpec


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
        print(f"Calorías: {r.calories}, Dificultad: {r.difficulty.value}\n")


if __name__ == "__main__":
    main()
