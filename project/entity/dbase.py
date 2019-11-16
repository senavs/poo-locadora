class SimpleTableDataBase(object):

    def __init__(self):
        self._DATA = {}

    def insert(self, data: dict):
        self._DATA[len(self._DATA)] = data

    def update(self, id: int, data: dict):
        if self._DATA.get(id):
            self._DATA[id] = data
            return True
        return False

    def delete(self, id: int):
        return self._DATA.pop(id, {})

    def select(self, id: int = None):
        if id is None:
            return self._DATA
        return self._DATA.get(id, {})

    def __repr__(self):
        return f'SimpleTableDataBase({len(self._DATA)})'
