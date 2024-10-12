sandwich_orders = [ "Pastrami","BLT", "PB&J", "Roast Beef",
                   "Pastrami","Tuna","Pastrami","Chicken Parm"]   
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        if sandwich == 'Pastrami':
            print('The deli has no Pastrami!')
            while sandwich in sandwich_orders:
                sandwich_orders.remove(sandwich)
        else:
            print(f'Making a {sandwich} now.')
            finished_sandwiches.append(sandwich)
            sandwich_orders.remove(sandwich)
print('\nAll sandwich orders have been filled.\nHere is the list of filled orders:')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')