
class users:
    def __init__ (self,first_name,last_name,company):

        self.first_name = first_name
        self.last_name = last_name 
        self.company = company    

    def describe_user(self):
        print(f'User: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}. Welcome back to {self.company}!')

user_1 = users('Mansor','Amond-Mansaray','Sony')
user_2 = users('Max','Styles','MAD DOG')
user_3 = users('John','Smith','MGM')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()