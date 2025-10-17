from Pizza import Pizza
from PizzaBuilder import PizzaBuilder

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        self.pizza.toppings = 'ham, pineapple'

    def get_pizza(self):
        return self.pizza

class CheeselessHawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        pass

    def add_toppings(self):
        self.pizza.toppings = 'ham, pineapple'

    def get_pizza(self):
        return self.pizza

class PestoPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'pesto sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        pass

    def get_pizza(self):
        return self.pizza

class GlutenFreeCheesePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def make_dough(self):
        self.pizza.dough = 'almond flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        pass

    def get_pizza(self):
        return self.pizza
