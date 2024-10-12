pizza_toppings = "\nPlease list your toppings:"
pizza_toppings += "\nEnter 'quit' to end your selection."

while True:
    toppings = input(pizza_toppings + "\n")
    if toppings.lower() == 'quit':
        break
    else:
        print(f'Will add {toppings} to your pizza.')