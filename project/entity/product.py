class Product(object):

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_quantity(self, value: int):
        self.quantity += value

    def __repr__(self):
        return f'Product{self.name, self.quantity}'
