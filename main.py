import pandas as pd

car_accident = pd.read_csv('data/database_car_accident.csv')
cities = pd.read_csv('data/comuni_italiani.csv', sep=';')
print(cities.info())

for name in list(cities):
    print(f'For the column {name} we have these unique values: ')
    print(cities[name].unique())