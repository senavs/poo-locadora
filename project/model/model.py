from project.entity.dbase import TableCollection

# Database
db = TableCollection()
# Client Table
db.add_table('client')
# Product Table
db.add_table('product')
# Register Table
db.add_table('register')
