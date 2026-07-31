import pandas as pd

#car_accident = pd.read_csv('data/database_car_accident.csv')
cities = pd.read_csv('data/comuni_italiani_2020.csv', sep=';')

#fix Null value in Comune column
comune_missing_value = cities[cities['Comune'].isnull()]
comune_missing_value['Comune'] = 'Torino'

#fix Null value in Cities column
sigla_missing_value = cities[cities['Sigla automobilistica'].isnull()]
sigla_missing_value['Sigla automobilistica'] = "NA"

