class Product(object):

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'Product{self.name, self.quantity}'
