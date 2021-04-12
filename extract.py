"""
    EXTRACT
    Através de uma URL de download obtemos o arquivo e salvamos em formato csv
"""
import requests

name_dataset = 'covid19.csv'
source_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

print('>>>> Extração iniciada <<<<')

data = requests.get(source_url)
if data.status_code != 200:
    print('Erro ao extrair!')

with open(f'download/{name_dataset}', 'w', encoding='utf-8') as f:
    f.write(data.text)
print('>>>> Extração finalizada <<<<')