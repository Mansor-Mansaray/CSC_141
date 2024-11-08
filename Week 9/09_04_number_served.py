# while using my code from exercise 09_01 I used
# default values to set a min and total number of 
# customers that were severed.
class restaurant:
    def __init__ (self, name, cuisine):

        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'\nRestaurant: {self.name}')
        print(f'Cuisine: {self.cuisine}')
        print(f'Customers Served: {self.number_served}')
    
    def open_restaurant(self):
        print(f'{self.name} is now open.')

    def set_number_served(self,number_served):
        self.number_served = number_served
    
    def increment_number_served(self,increment):
        self.number_served += increment

Restaurant = restaurant('TGI Friday','Burgers')

Restaurant.describe_restaurant()
Restaurant.set_number_served(900)
Restaurant.describe_restaurant()
Restaurant.increment_number_served(200)
Restaurant.describe_restaurant()