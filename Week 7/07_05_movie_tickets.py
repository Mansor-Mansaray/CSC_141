while True:
    age = int(input('\nWhat is your age?\nEnter "000" to exit '))
    
    if age == 000:
        break
    if age < 3:
        print('Your ticket is free!')
    if age >= 3:
        if age < 12:
            print('Your ticket is $10.')
    if age >= 12:
        print('Your ticket is $15.')