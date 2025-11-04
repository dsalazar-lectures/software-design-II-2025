from src.Shared.Logger_component import CustomLogger

logger = CustomLogger()

def main():
    user="Yordi"
    logger.log(
        level="info",
        usuario="Yordi",
        rol="Admin",
        accion="Login",
        descripcion=f"{user} logged in successfully"
    )

if __name__ == "__main__":
    main()
