class Despensa:
    @staticmethod
    def ingredientes_faltantes(requeridos, disponibles):
        """Devuelve lista de ingredientes faltantes"""
        return [i for i in requeridos if i not in disponibles]
