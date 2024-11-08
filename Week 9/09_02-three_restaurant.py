class restaurant:
    def __init__ (self, name, cuisine):

        self.name = name
        self.cuisine = cuisine

describe_restaurant = restaurant('TGI Friday','Burgers')
describe_restaurant01 = restaurant('The Cheesecake Factory','Cheesecake')
describe_restaurant02 = restaurant('Olive Garden','Salad')


print(f"My favorite restaurant for burgers is {describe_restaurant.name}")
print(f"There {describe_restaurant.cuisine} is to die for.")

print(f"{describe_restaurant01.name} is the best place for {describe_restaurant01.cuisine}.")
print(f"I love {describe_restaurant01.cuisine}.")

print(f"{describe_restaurant02.name} is great place to have dinner with family and friends.")
print(f"They have great {describe_restaurant02.cuisine} to start off your meal.")


open_restaurant = restaurant('TGI Friday', '11am')
open_restaurant01 = restaurant('Olive Garden', '10:00am')
open_restaurant02 = restaurant('The Cheesecake Factory', '11:30am')

print(f"{open_restaurant.name} opens at {open_restaurant.cuisine}.")
print(f"{open_restaurant01.name} opens at {open_restaurant01.cuisine}.")
print(f"{open_restaurant02.name} opens at {open_restaurant02.cuisine}.")
