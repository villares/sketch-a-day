import py5
import requests
from random import sample
# headers = {
#     'Content-Type': 'application/json;charset=UTF-8',
#     }
distritos = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos?orderBy=nome'
request = requests.get(distritos)#, headers=headers)
json_ibge = request.json()
print(len(json_ibge))

def extract(record):
    return "{}  - {} - {}".format(
        record['nome'],
        record['municipio']['nome'],
        record['municipio']['microrregiao']['nome']
        )

def setup():
    py5.size(600, 600)
    py5.text_size(20)
    py5.fill(0)
    for record in sample(json_ibge, 10):
        distrito_municipio_microrregiao = extract(record)
        py5.text(distrito_municipio_microrregiao, 20, 40)
        py5.translate(0, 30)

py5.run_sketch()