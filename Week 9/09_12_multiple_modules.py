from imp_09_12_multiple_modules_01 import Users
from imp_09_12_multiple_modules_02 import *

user_1 = Users('Mary','Jane')
user_1.describe_user()
user_1.greet_user()

admin_1 = Admin('Mansor','Amond-Mansaray')
admin_1.describe_admin()
admin_1.privileges.show_privileges()