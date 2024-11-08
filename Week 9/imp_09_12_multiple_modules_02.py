class Admin:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()

    def describe_admin(self):
        print(f'{self.first_name} {self.last_name} is the Admin')

    def greet_admin(self):
        print(f'Hello {self.first_name} {self.last_name}!')

class Privileges():

    def __init__(self):
        self.privileges = ['can make posts', 'can delete posts', 'can ban users']

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(privilege)