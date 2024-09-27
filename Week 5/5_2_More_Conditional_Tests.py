pet = 'cat'
print("Is pet == 'fish'? I predict False.")
print(pet == 'fish')
print("Is pet == 'cat'? I predict True.")
print(pet == 'cat')

pet = 'dog'
print("Is pet == 'snake'? I predict False.")
print(pet == 'snake')
print("Is pet == 'dog'? I predict True.")
print(pet == 'dog')

pet = 'turtle'
print("Is pet == 'bunny'? I predict False.")
print(pet == 'bunny')
print("Is pet == 'turtle'? I predict True.")
print(pet == 'turtle')

pet = 'parrot'
print("Is pet == 'lizard'? I predict False.")
print(pet == 'lizard')
print("Is pet == 'parrot'? I predict True.")
print(pet == 'parrot')

pet = 'hamster'
print("Is pet == 'mouse'? I predict False.")
print(pet == 'mouse')
print("Is pet == 'hamster'? I predict True.")
print(pet == 'hamster')

cake = 'cheesecake'
cake == 'cheesecake'

toppings = 'Starwbeerry'
toppings == 'Mango'

drinks = ['WATER', 'PEPSI', 'SPRITE', 'DR.PEPPER']

for drink in drinks:
  if drink == 'PEPSI':
      print(drink.lower())
  else:
      print(drink.title())



price_0 = 30
price_1 = 25
price_0 >= 30 and price_1 <= 45

price_3 = 20
price_4 = 11
price_3 < 29 or price_4 > 4

Shoe_Brands = ['Nike', 'Jordan', 'Under Armor', "Addidas"]
'Jordan' in Shoe_Brands
'Fila' in Shoe_Brands

vip_seats = ['Jake', 'Peter', 'Nick', 'Jacob']
vip = 'fred'
if vip not in vip_seats:
  print(f"{vip.title()}, you can't come into the vip section.")