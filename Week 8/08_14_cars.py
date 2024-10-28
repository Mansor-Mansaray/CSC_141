def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_1 = make_car('Infiniti', 'QX50', color='grey',
                  tow_package=True)
car_2 = make_car('Lexus', 'LX', color='black', 
                 tow_package=False)
print(car_1)
print(car_2)