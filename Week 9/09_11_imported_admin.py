from imp_09_11_imported_admin import User, Admin

user_1 = User('Mary', 'Jane', 25)
user_1.describe_user()
user_1.greet_user()

admin_1 = Admin('Mansor', 'Amond-Mansaray', 20)
admin_1.describe_user()  
admin_1.privileges.show_privileges()