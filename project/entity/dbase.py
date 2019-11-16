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


class TableCollection(object):

    def __init__(self):
        self._TABLE_COLLECTION = {}

    def add_table(self, table_name):
        if table_name not in self._TABLE_COLLECTION:
            self._TABLE_COLLECTION[table_name] = SimpleTableDataBase()
            return True
        return False

    def __getitem__(self, table_name: str):
        return self._TABLE_COLLECTION.get(table_name)

    def __setitem__(self, table_name: str, table: SimpleTableDataBase):
        if not isinstance(table, SimpleTableDataBase):
            raise ValueError(f'Table must be a SimpleTableDataBase instance')
        self._TABLE_COLLECTION[table_name] = table

    def __repr__(self):
        return f'TableCollection({len(self._TABLE_COLLECTION)})'
