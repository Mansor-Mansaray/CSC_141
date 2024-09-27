current_users = ['CrisRoxs', 'TheOnlyOne', 'Rex42',
                 'Mr.Jay11', 'Mr.Cheesecake']

current_users = ['crisroxs', 'theonlyone', 'rex42',
                'mr.jay11', 'mr.cheesecake']




new_users = ['Kilmonger23', 'ItsJeff', 'Mr.Cheesecake',
             'Potter4Ever', 'JBond007']

for new_users in new_users:
 if new_users in current_users:
   print(f"You need to update your username {new_users}.")
else:
 print(f"Welcome back, {new_users}.")