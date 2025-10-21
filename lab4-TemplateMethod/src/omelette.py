from plantillaReceta import PlantillaReceta

class Omelette(PlantillaReceta):
    def ingredientes_requeridos(self):
        return ["huevos", "queso", "jamon"]

    def pasos_preparacion(self):
        print(
            " - Batir los huevos con una pizca de sal\n"
            " - Rallar/trozear el queso y cortar el jamón en cuadritos o tiritas\n"
            " - Precalentar sartén y engrasar con un poco de aceite"
        )

    def cocinar(self):
        print(
            "Verter los huevos batidos; cuando cuaje por bordes y el centro siga jugoso,\n"
            "repartir jamón y queso; doblar en media luna y cocinar 1–2 min más según el punto deseado."
        )

    def decorar(self):
        print("Echarle un poco de pimienta y un toque de perejil picado.")
