import happybase as hb

connection = hb.Connection('localhost')
connection.open()

families1 = {
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
}

connection.create_table('powers', families1)


families2 = {
    'nutrition': dict(),
    'taste': dict()
}

connection.create_table('food', families1)

