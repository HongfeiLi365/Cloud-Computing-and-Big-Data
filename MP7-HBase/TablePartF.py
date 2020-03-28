import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection('localhost')
connection.open()

table = connection.table('powers')

for key1, data1 in table.scan():
    for key2, data2 in table.scan():
        if (data1['custom:color'] == data2['custom:color']) and (data1['professional:name'] != data2['professional:name']):
            color = data1['custom:color']
            name = data1['professional:name']
            power = data1['personal:power']

            color1 = data2['custom:color']
            name1 = data2['professional:name']
            power1 = data2['personal:power']

            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))


