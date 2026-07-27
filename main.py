import requests

#url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"
url = 'https://esploradati.istat.it/SDMXWS/rest/data/41_983'

print("starting the script")
data = requests.get(url, headers={'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}, stream=True)
print('starting scraping of data')
data.raise_for_status()


