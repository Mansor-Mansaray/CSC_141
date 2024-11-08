
class Users:
    def __init__(self, first_name, last_name, company):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company    
        self.login_attempts = 0 

    def describe_user(self):
        print(f'User: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}. Welcome back to {self.company}!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating instances of Users
user_1 = Users('Mansor', 'Amond-Mansaray', 'Sony')
user_2 = Users('Max', 'Styles', 'MAD DOG')
user_3 = Users('John', 'Smith', 'MGM')

# Calling methods for each user
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

# Incrementing login attempts for user_1
user = Users('Mansor', 'Amond-Mansaray', 'Sony')
for i in range(20):
    user.increment_login_attempts()
print(f'Login Attempts: {user.login_attempts}')

# Resetting login attempts
user.reset_login_attempts()
print(f'Login Attempts: {user.login_attempts}')
