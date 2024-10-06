cities = {
    "Seattle": {
        "country": "USA",
        "population": 749256,
        "fact": "Seattle is known for the Space Needle."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13960000,
        "fact": "Tokyo is the most populated city in the world."
    },
    "Ontario": {
        "country": "Canada",
        "population": 293000000,
        "fact": "Ontario is known for Niagara Falls."}
}

for city_name, info in cities.items():
    for city in city_name:
        country = info['country']
        population = info['population']
        fact = info['fact']
    print(city_name)
    print(f'\tCountry: {country}')
    print(f'\tPopulation: {population}')
    print(f'\tFun Fact: {fact}')
