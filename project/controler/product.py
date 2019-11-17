from project.entity.product import Product
from project.model.model import db


class ProductController(object):

    @staticmethod
    def insert_product(product: Product):
        return db['product'].insert(product.__dict__)

    @staticmethod
    def update_product(id: int, product: Product):
        return db['product'].update(id, product.__dict__)

    @staticmethod
    def delete_product(id: int):
        return db['product'].delete(id)

    @staticmethod
    def select_product(id: int):
        return db['product'].select(id)

    @staticmethod
    def list_products():
        return db['product'].select()

    @classmethod
    def add_quantity_product(cls, id: int, value: int):
        product = cls.select_product(id)
        if product:
            product = Product(product)
            product.add_quantity(value)
            cls.update_product(id, product)
            return True
        return False
