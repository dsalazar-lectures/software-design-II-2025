from PizzaBuilder import PizzaBuilder

class HawaiianPizzaBuilder(PizzaBuilder):
    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        self.pizza.toppings = 'ham, pineapple'

class CheeselessHawaiianPizzaBuilder(PizzaBuilder):
    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        pass

    def add_toppings(self):
        self.pizza.toppings = 'ham, pineapple'

class PestoPizzaBuilder(PizzaBuilder):
    def make_dough(self):
        self.pizza.dough = 'wheat flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'pesto sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        pass

class GlutenFreeCheesePizzaBuilder(PizzaBuilder):
    def make_dough(self):
        self.pizza.dough = 'almond flour dough'

    def add_sauce(self):
        self.pizza.sauce = 'tomato sauce'

    def add_cheese(self):
        self.pizza.cheese = 'mozzarella'

    def add_toppings(self):
        pass
