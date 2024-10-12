sandwich_orders = [ "BLT", "PB&J", "Roast Beef", "Tuna", "Chicken Parm"]   
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f'Making a {sandwich} now.')
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)

print('\nAll sandwich orders are completed.\nHere are the orders:')
for sandwich in finished_sandwiches:
    print(f'>{sandwich}')