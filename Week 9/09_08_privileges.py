class Admin:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_admin(self):
        print(f'Admin: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

class Privileges(Admin):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add posts', 'can delete posts', 'can ban users']

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(privilege)

admin_privileges = Privileges('Mansor','Amond-Mansaray')
admin_privileges.show_privileges()