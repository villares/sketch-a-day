"""
Dados do CSV vem do Senso Escolar baixados com um script em 
https://github.com/villares/mestrado/tree/master/dados-escolas
inspirado no material do prof. Fernando Masanori
Exemplo da API:
http://educacao.dadosabertosbr.com/api/estatisticas?tipoLocal=MUN&codMunicipio=5300108
    {'televisores': '1.75',
     'ano': '2013', 'datashows': '1.25',
     'salasUtilizadas': '3.5',
     'laboratorioInformatica': '0.5',
     'bandaLarga': '0.25', 'internet': '0.5',
     'codMunicipio': '5300108',
     'computadoresAlunos': '9.0'}
"""

import csv

def setup():
    size(500, 500)
    noFill()
    with open("dados-municipios-2013.csv") as f:
        data = list(csv.DictReader(f))
    print data
    print(len(data))

    w = width / 75.0
    for i in range(75):
        x = w / 2 + i * w
        for j in range(75):
            y = w / 2 + j * w
            if data:
                d = data.pop()
                n = d.get('computadoresAlunos', 0)
                # print(n)
                circle(x, y, float(n))

    # with open("dados-municipios-2013.csv") as f:
    #     statsData = csv.reader(f)
    #     for row in statsData:
    #         for c in row:
    #             print(unicode(c, encoding='utf-8'))
