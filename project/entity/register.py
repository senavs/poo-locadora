from project.entity.client import Client
from project.entity.product import Product


class Register(object):

    def __init__(self, client: Client, product: Product):
        self.client = client
        self.product = product

    def __repr__(self):
        return f'Register{self.client, self.product}'
