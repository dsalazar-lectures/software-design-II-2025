from abc import ABC, abstractmethod
from despensa import Despensa

class PlantillaReceta(ABC):
    """Template Method: define la secuencia fija para cocinar una receta"""
    # Ingredientes mínimos obligatorios para cualquier receta
    base_requeridos = ["sal", "aceite"]

    def cocinar_receta(self, despensa):
        if not self.verificar_ingredientes(despensa):
            return False
        
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
            lista = ", ".join(faltantes)
            print(f"No se puede preparar {self.__class__.__name__}: faltan {lista}")
            print(f"Agrega esos ingredientes a tu despensa e inténtalo de nuevo.\n")
            return False
        print("Tienes todos los ingredientes :)")
        return True

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
