from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
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

    @abstractmethod
    def get_pizza(self):
        pass
