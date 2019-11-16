from project.entity.client import Client
from project.model.model import db


class ClientController(object):

    @staticmethod
    def insert_client(client: Client):
        return db['client'].insert(client.__dict__)

    @staticmethod
    def update_client(id: int, client: Client):
        return db['client'].update(id, client.__dict__)

    @staticmethod
    def delete_client(id):
        return db['client'].delete(id)

    @staticmethod
    def select_client(id):
        return db['client'].select(id)

    @staticmethod
    def list_clients():
        return db['client'].select()

    @classmethod
    def add_debt_client(cls, id, value):
        client = Client(**cls.select_client(id))
        if client:
            client.add_debt(value)
            cls.update_client(id, client)
            return True
        return False

    @classmethod
    def reset_debit_client(cls, id):
        client = Client(**cls.select_client(id))
        if client:
            client.reset_debt()
            cls.update_client(id, client)
            return True
        return False
