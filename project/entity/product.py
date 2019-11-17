class Product(object):

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_quantity(self, value: int):
        if self.quantity + value < 0:
            self.quantity = 0
        else:
            self.quantity += value

    def __repr__(self):
        return f'Product{self.name, self.quantity}'
