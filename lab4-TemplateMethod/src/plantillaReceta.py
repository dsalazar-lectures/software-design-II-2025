from abc import ABC, abstractmethod
from despensa import Despensa

class PlantillaReceta(ABC):
    """Template Method: define la secuencia fija para cocinar una receta"""
    # Ingredientes mínimos obligatorios para cualquier receta
    base_requeridos = ["sal", "aceite"]

    def cocinar_receta(self, despensa):
        self.verificar_ingredientes(despensa)
        self.preparacion(despensa)
        self.cocinar()
        self.emplatar()
        self.decorar()
        print("Listo, a disfrutar!\n")

    # Pasos fijos
    def verificar_ingredientes(self, despensa):
        requeridos = set(self.base_requeridos) | set(self.ingredientes_requeridos())
        faltantes = Despensa.ingredientes_faltantes(requeridos, despensa)
        if faltantes:
            raise ValueError(f"Faltan ingredientes: {', '.join(faltantes)}")
        print("Tienes todos los ingredientes :)")

    # Paso fijo que llama a pasos_preparacion()
    def preparacion(self, despensa):
        print("Preparación: lavar / cortar / pesar…")
        self.pasos_preparacion()

    def emplatar(self):
        print("Emplatando…")

    # Pasos que se pueden personalizar por cada receta
    @abstractmethod
    def ingredientes_requeridos(self):
        return []

    @abstractmethod
    def pasos_preparacion(self):
        ...

    @abstractmethod
    def cocinar(self):
        ...

    # Hook opcional
    def _decorar(self):
        pass
