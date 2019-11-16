class Client(object):

    def __init__(self, id_number: str, name: str, address: str, phone: str):
        self.id_number = id_number
        self.name = name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return f'Client{self.id_number, self.name, self.address, self.phone}'
