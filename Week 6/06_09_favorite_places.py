favorite_places = {
    'Mansor' : ['My bed', 'The Cheesecake Factory', 'Japan'],
    'Markus' : ['Spain', 'Toranto', 'Utah'],
    'Mason' : ['Canada', 'L.A.', 'Brazil']}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")
    for place in places:
        print(f'{place}')
