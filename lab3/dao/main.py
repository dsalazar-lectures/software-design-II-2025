from recipe_dao_impl import RecipeDAOImpl

def main():
    dao = RecipeDAOImpl()

    # Crear
    r1 = dao.create("Pasta al Pesto", ["pasta", "albahaca", "aceite de oliva"], "Jose")
    r2 = dao.create("Sándwich", ["pan", "queso", "jamón"], "Luis")
    print("Creado:", r1)
    print("Creado:", r2)

    # Leer por id
    print("\nPor id 1:", dao.get_by_id(1))

    # Actualizar
    print("\nActualizando receta 2:")
    updated = dao.update(2, name="Sándwich de queso", ingredients=["pan", "queso", "jamón", "mantequilla"])
    print("Actualizado:", updated)

    # Eliminar
    print("\nEliminando receta 1:")
    print("Eliminado:", dao.delete(1))

    print("\nRecetas:")
    for r in dao.get_all():
        print(" -", r)


if __name__ == "__main__":
    main()

