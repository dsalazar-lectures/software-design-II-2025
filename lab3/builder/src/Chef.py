from PizzaBuilder import PizzaBuilder

class Chef:
    def make_pizza(self, builder: PizzaBuilder):
        builder.make_dough()
        builder.add_sauce()
        builder.add_cheese()
        builder.add_toppings()
        return builder.get_pizza()
