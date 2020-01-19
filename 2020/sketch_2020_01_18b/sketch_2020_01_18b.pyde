from __future__ import unicode_literals
from fundo import fundo
add_library('pdf')

modelo = "poster"
nomes = [
    """PCD
2020
SP""",
]

def setup():
    global modelo, frente, f, img
    size(400, 600)
    f = createFont('Ubuntu', 150)  # precisa ter Tomorrow M instalada
    img = draw_text(nomes[0], width / 2, height / 2)

def draw():
    image(img, 0, 0)
    fundo(nomes[0], img)

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
