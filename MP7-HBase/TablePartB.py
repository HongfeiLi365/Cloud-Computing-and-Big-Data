import happybase as hb

connection = hb.Connection('localhost')
connection.open()

print connection.tables()