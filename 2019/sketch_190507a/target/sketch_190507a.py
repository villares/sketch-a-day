"""
Alexandre B A Villares - abav.lugaralgum.com/sketch-a-day
"""

from pyp5js import *

sliders = []

def setup():
    P5 = _P5_INSTANCE
    createCanvas(windowWidth, windowHeight)
    #createCanvas(600, 600)
    for i in range(4):
        s = P5.createSlider(0, 64, 0)
        s.position(10, i * 30)
        s.style("width", "200px")
        sliders.append(s)
    rectMode('center')  # retângulos desenhados pelo centro
    colorMode('hsb', 255, 255, 255)  
    strokeWeight(2)  # espessura de linha 2px
    noFill()  # sem preenchimento
    frameRate(30)  # deixa um pouco mais lento
    
def draw():
    background(200)  # fundo cinza claro

    grid_elem = 5 + sliders[0].value()
    elem_size = 5 + sliders[1].value()
    rand_size = sliders[2].value()
    rand_posi = sliders[3].value()
    
    # trava a randomização entre os ciclos de draw
    # mas varia com o número de colunas na grade
    randomSeed(int(grid_elem / 4))
    # calcula o espaçamento entre os quadrandos
    spac_size = int(width / (grid_elem + 1))
    # para cada coluna um x
    for x in range(spac_size / 2, width, spac_size):
        # para cada linha um y
        for y in range(spac_size / 2, width, spac_size):
            # sorteia um tamanho (se o rand_size > 0)
            square_size = elem_size + rand_size * random(-1, 1)
            stroke(square_size * 3, 255, 128)
            rect(x + rand_posi * random(-1, 1),  # desenha um quadrado
                 y + rand_posi * random(-1, 1),
                 square_size,
                 square_size)

# def mousePressed():
#     global grid_elem

# This is required by pyp5js to work
start_p5(setup, draw)
