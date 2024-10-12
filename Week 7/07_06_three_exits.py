pizza_toppings = '\nWhat toppings would you like added to your pizza?'
pizza_toppings += '\nIf none, enter "quit" to exit. '
i = 0 

while i < 3: 
    toppings = input(pizza_toppings)
    if toppings.lower() == 'quit':
        break
    else:
        print(f'Will add {toppings} to your pizza.')
    i += 1