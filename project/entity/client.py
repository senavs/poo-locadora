class Client(object):

    def __init__(self, id_number: str, name: str, address: str, phone: str):
        self.id_number = id_number
        self.name = name
        self.address = address
        self.phone = phone
        self.debt = 0

    def __repr__(self):
        return f'Client{self.id_number, self.name, self.address, self.phone}'

    def add_debt(self, value):
        self.debt += value

    def reset_debt(self):
        self.debt = 0
