person1 = {'first_name' : 'Bryan',  'last_name' : 'Gonzalas', 'age' : 19, 'city' : 'Silver Spring'}

person2 = {'first_name': 'Josalyn', 'last_name': 'Nnee', 'age': 19, 'city': 'Wheaton',}

person3 = {'first_name': 'Micheal', 'last_name': 'Cruz', 'age': 19, 'city': 'Takoma Park'}

people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"\n{full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")