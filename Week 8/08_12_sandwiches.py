def make_sandwich(*items):
    print('\nMaking your sandwich with:')
    for item in items:
        print(f'- {item.title()}')

make_sandwich('Nutella')
make_sandwich('Penut Butter','Jelly')
make_sandwich('Chicken','bacon','Cheese')