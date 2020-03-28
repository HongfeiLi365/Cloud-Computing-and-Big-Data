import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection('localhost')
connection.open()

table = connection.table('powers')

row = table.row('row1')

hero = row['personal:hero']
power = row['personal:power']
name =  row['professional:name']
xp =  row['professional:xp']
color =  row['custom:color']

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

row = table.row('row19')

hero = row['personal:hero']
color = row['custom:color']

print('hero: {}, color: {}'.format(hero, color))

row = table.row('row1')

hero = row['personal:hero']
name = row['professional:name']
color = row['custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))