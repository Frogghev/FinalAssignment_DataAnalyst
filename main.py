import pandas as pd

car_accident = pd.read_csv('data/database_car_accident.csv')
print(car_accident.info())

for name in list(car_accident):
    print(f'For the column {name} we have these unique values: ')
    print(car_accident[name].unique())