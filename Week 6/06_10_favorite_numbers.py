favorite_numbers = {'otto': [1,2,3], 'max' : [19,22,32], 'kevin' : [21,72,93], 'ian' : [77,93,2035],'pedro' : [87,34,89]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(number)