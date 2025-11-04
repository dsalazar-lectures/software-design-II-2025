from src.Shared.Logger_component import CustomLogger

logger = CustomLogger()

def main():
    result1 = "Pasta Alfredo #123"
    logger.log(
        level="info",
        usuario="Alice",
        rol="Chef",
        accion="Add recipe",
        descripcion=f"Recipe added successfully: {result1}"
    )

if __name__ == "__main__":
    main()
