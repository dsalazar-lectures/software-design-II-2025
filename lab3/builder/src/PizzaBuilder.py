from abc import ABC, abstractmethod
from Pizza import Pizza

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def make_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

    def get_pizza(self):
        pizza = self.pizza
        self.pizza = Pizza()
        return pizza
