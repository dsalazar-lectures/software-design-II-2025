from pancakes import Pancakes
from omelette import Omelette

if __name__ == "__main__":
    despensa = {
        "sal","pimienta","huevos","queso","tocino","harina","jamon","azucar","mantequilla","aceite","vainilla","polvo_de_hornear","leche"
    }

    print("\n==>", Pancakes.__name__)
    Pancakes().cocinar_receta(despensa)

    print("\n==>", Omelette.__name__)
    Omelette().cocinar_receta(despensa)