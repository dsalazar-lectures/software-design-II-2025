from plantillaReceta import PlantillaReceta

class Pancakes(PlantillaReceta):
    def ingredientes_requeridos(self):
        return ["harina", "azucar", "huevos", "leche", "polvo_de_hornear", "vainilla"]

    def pasos_preparacion(self):
        print(
            " - Mezclar harina, azúcar, sal y polvo de hornear\n"
            " - Aparte, batir huevos, leche y vainilla; integrar con la harina y mezclar hasta que quede sin grumos\n"
            " - Engrasar la sartén con un poco de aceite"
        )

    def cocinar(self):
        print(
            "Verter pequeñas porciones en el sartén a fuego medio; cuando salgan burbujas, voltear.\n"
            "Cocinar 1–2 min más hasta dorar."
        )

    def decorar(self):
        print("Servir con miel, fruta, crema batida o helado.")
