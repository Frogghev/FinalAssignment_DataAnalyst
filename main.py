import pandas as pd

#car_accident = pd.read_csv('data/database_car_accident.csv')
cities = pd.read_csv('data/comuni_italiani.csv', sep=';')

print(cities.shape)

#print(cities[cities['Comune'].isnull()])