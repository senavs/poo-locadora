from project.entity.client import Client
from project.controler.client import ClientController
from project.entity.product import Product
from project.controler.product import ProductController
from project.entity.register import Register
from project.model.model import db


class RegisterController(object):

    @staticmethod
    def rent_product(id_client: int, id_product: int):
        # verify if client or product exist
        client = ClientController.select_client(id_client)
        product = ProductController.select_product(id_product)
        if not client or not product:
            return False

        # decrease product quantity
        client = Client(**client)
        product = Product(**product)
        if product.quantity > 0:
            product.add_quantity(-1)
            ProductController.update_product(id_product, product)
        else:
            return False
        register = Register(client, product)
        return db['register'].insert(register.__dict__)

    @classmethod
    def give_product_back(cls, id_register: int, id_client: int, id_product: int):
        register = cls.select_register(id_register)
        product = ProductController.select_product(id_product)
        client = ClientController.select_client(id_client)
        if register and product and client:
            product = Product(**product)
            product.add_quantity(1)
            ProductController.update_product(id_product, product)
            cls.delete_register(id_register)
            return True
        return False

    @staticmethod
    def give_client_fine(id_client: int, value: int):
        return ClientController.add_debt_client(id_client, value)

    @staticmethod
    def remove_client_fine(id_client: int):
        return ClientController.reset_debit_client(id_client)

    @staticmethod
    def delete_register(id_register: int):
        return db['register'].delete(id_register)

    @staticmethod
    def select_register(id: int):
        return db['register'].select(id)

    @staticmethod
    def list_registers():
        return db['register'].select()
