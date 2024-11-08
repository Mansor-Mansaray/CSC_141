class restaurant:
    def __init__ (self, name, cuisine):

        self.name = name
        self.cuisine = cuisine

describe_restaurant = restaurant('TGI Friday','Burgers')

print(f"My favorite restaurant for burgers is {describe_restaurant.name}")
print(f"There {describe_restaurant.cuisine} is to die for.")

open_restaurant = restaurant('TGI Friday', '11am')

print(f"{open_restaurant.name} opens at {open_restaurant.cuisine}.")