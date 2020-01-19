from __future__ import unicode_literals, division
from fundo import fundo
add_library('pdf')

modelo = "poster"
nomes = [
"""PCD
2020
SP""",
         ]

def setup():
    global modelo, frente, f
    size(400, 600)
    noLoop()
    f = createFont('Tomorrow-Medium', 140)  # precisa ter Tomorrow M instalada

def draw():
    pdf = createGraphics(width, height, PDF, "{}-{}.pdf".format(modelo, "PCD20SP"))
    beginRecord(pdf)
    for nome in nomes:
        img = draw_text(nome, width / 2, height / 2)
        fundo(nome, img)
        if nome != nomes[-1]:
            pdf.nextPage()            
    endRecord()
    # exit()  # fecha o sketch!
    saveFrame("###.png")

def draw_text(txt, x, y, text_size=250):
    img = createGraphics(width, height)
    img.beginDraw()
    img.textFont(f)
    img.textAlign(CENTER, CENTER)
    img.textSize(text_size)
    img.textFont(f)
    img.text(txt, x, y)
    img.endDraw()
    return img
