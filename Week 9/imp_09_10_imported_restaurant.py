
class Restaurant:


    def __init__(self, name, cuisine_type):
        
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
    
        print(f"{self.name} serves great {self.cuisine_type}.")

    def open_restaurant(self):
    
        print(f"{self.name} is now open!")
