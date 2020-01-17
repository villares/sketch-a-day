from __future__ import unicode_literals
from fundo import fundo
add_library('pdf')

modelo = "moldura"
nomes = ["PCD",
         "São Paulo",
         "2020",
         ]

def setup():
    global modelo, frente, f
    size(500, 500)
    noLoop()
    # frente = loadShape(modelo + '.svg')
    # Use createFont() instead of loadFont() when drawing text using the PDF library.
    f = createFont('Tomorrow-Medium', 54)  # precisa ter Tomorrow M instalada

def draw():
    pdf = createGraphics(width, height, PDF, "{}-{}.pdf".format(modelo, "PCD20SP"))
    beginRecord(pdf)
    for nome in nomes:
        fundo(nome)
        # shape(frente)
        textFont(f)
        textSize(400 / len(nome))
        fill(0)
        textAlign(CENTER, CENTER)
        text(nome, width / 2, height / 2)
        if nome != nomes[-1]:
            pdf.nextPage()            
    endRecord()
    # exit()  # fecha o sketch!
    
