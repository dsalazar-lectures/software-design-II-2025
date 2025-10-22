from Chef import Chef
from ConcreteBuilders import HawaiianPizzaBuilder, CheeselessHawaiianPizzaBuilder, PestoPizzaBuilder, GlutenFreeCheesePizzaBuilder


if __name__ == "__main__":
    chef = Chef()
    hawaiianPizzaBuilder = HawaiianPizzaBuilder()
    cheeselessHawaiianPizzaBuilder = CheeselessHawaiianPizzaBuilder()
    pestoPizzaBuilder = PestoPizzaBuilder()
    glutenFreeCheesePizzaBuilder = GlutenFreeCheesePizzaBuilder()

    hawaiianPizza = chef.make_pizza(hawaiianPizzaBuilder)

    cheeselessHawaiianPizza = chef.make_pizza(cheeselessHawaiianPizzaBuilder)

    pestoPizza = chef.make_pizza(pestoPizzaBuilder)

    glutenFreeCheesePizza = chef.make_pizza(glutenFreeCheesePizzaBuilder)

    print(hawaiianPizza)
    print(cheeselessHawaiianPizza)
    print(pestoPizza)
    print(glutenFreeCheesePizza)
