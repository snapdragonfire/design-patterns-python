class Burger:
    def __init__(self, size, cheese=False, pepperoni=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni


class BurgerBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def build(self):
        return Burger(self.size, self.cheese, self.pepperoni)


builder = BurgerBuilder(4)
burger = builder.add_cheese().add_pepperoni().build()
