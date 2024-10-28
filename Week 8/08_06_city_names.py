def city_country(city, country):
    message = (f"'{city.title()}, {country.title()}'")
    return message

message = city_country('Tokyo', 'Japan')
print(message)

message = city_country('Maryland', 'United States')
print(message)

message = city_country('Hamburg', 'Germany')
print(message)