import logging
from typing import List, Optional
import uuid


class CustomLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance._instance_id = f"SID-{uuid.uuid4().hex[:8]}"
            print(
                f"\n\n        [INFO] Singleton CustomLogger inicializado con ID: {cls._instance._instance_id}"
            )
        else:
            print(
                f"\n        [INFO] Reutilizando Singleton existente con ID: {cls._instance._instance_id}"
            )
        return cls._instance

    def __init__(
        self, name: str = "AppLogger", handlers: Optional[List[logging.Handler]] = None
    ):
        if getattr(self, "_initialized", False):
            return

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if handlers is None:
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | Usuario: %(usuario)s | "
                "Rol: %(rol)s | Acción: %(accion)s | Descripción: %(descripcion)s",
                "%Y-%m-%d %H:%M:%S",
            )
            console.setFormatter(formatter)
            handlers = [console]

        if not self.logger.handlers:
            for h in handlers:
                self.logger.addHandler(h)

        self._initialized = True

    def add_file_handler(self, filepath: str):
        if any(
            isinstance(h, logging.FileHandler)
            and getattr(h, "baseFilename", "").endswith(filepath)
            for h in self.logger.handlers
        ):
            return
        fh = logging.FileHandler(filepath, encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | Usuario: %(usuario)s | "
                "Rol: %(rol)s | Acción: %(accion)s | Descripción: %(descripcion)s",
                "%Y-%m-%d %H:%M:%S",
            )
        )
        self.logger.addHandler(fh)

    def log(self, level: str, usuario: str, rol: str, accion: str, descripcion: str):
        extra = {
            "usuario": usuario,
            "rol": rol,
            "accion": accion,
            "descripcion": descripcion,
        }
        method = {
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "debug": self.logger.debug,
        }.get(level.lower(), self.logger.info)
        method("", extra=extra)
