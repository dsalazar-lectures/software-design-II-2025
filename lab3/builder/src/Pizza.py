class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None

    def __str__(self):
        return f'Dough: {self.dough}, Sauce: {self.sauce}, Cheese: {self.cheese} Toppings: {self.toppings}'