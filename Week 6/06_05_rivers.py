rivers = { 'ganges' : 'asia', 'niger' : 'africa', 'mississippi' : 'united states'}

for k,v in rivers.items():
    print(f'The {k.title()} River is in {v.title()}.')
print('\n')

for river in rivers:
    print(river.title())
print('\n')

for value in rivers.values():
    print(value.title())
