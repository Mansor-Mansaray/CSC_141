pet1 = {'animal' : 'hamster', 'owner' : 'noah'}
pet2 = {'animal' : 'cat', 'owner' : 'sara'}
pet3 = {'animal' : 'lizard', 'owner' : 'timmy'}

pets = [pet1,pet2,pet3]

for pet in pets:
    for k,v in pet.items():
        animal_type = pet['animal']
        owner_name = pet['owner']

    print(f'\nAnimal: {animal_type.title()}')
    print(f'Owner: {owner_name.title()}')