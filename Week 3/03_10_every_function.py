Fruits = ['Starwberry', 'Blueberry', 'Grapes', 'Mangos', 'Watermelon']

print(Fruits[3])
print(Fruits[1])

message = f"I love eating {Fruits[2].title()}."
print(message)

Fruits[1] = 'DragonFruit'
print(Fruits)

Fruits.append('Apple')
print(Fruits)

Fruits.insert(3, 'Orange')
print(Fruits)

del Fruits[4]
print(Fruits)

popped_Fruit = Fruits.pop()
print(Fruits)
print(popped_Fruit)

Ripe_Fruit = Fruits.pop(1)
print(f"This {Ripe_Fruit.title()} is to ripe")

Fruits.remove('Grapes')
print(Fruits)

Fruits.sort()
print(Fruits)

print(sorted(Fruits))

Fruits.reverse()
print(Fruits)

print(len(Fruits))
