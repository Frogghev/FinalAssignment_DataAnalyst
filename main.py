import requests

url = 'https://esploradati.istat.it/SDMXWS/rest/data/41_983'
header = {'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}
params = {
    'startPeriod' : '2020'
}

data = requests.get(url, headers=header, params=params, stream=True)
data.raise_for_status()

with open("database_car_accident.csv", 'w') as file:
    file.write(data.text)



