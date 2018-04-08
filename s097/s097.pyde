# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s097"  # 180407

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    size(600, 600)
    frameRate(30)
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino)

def draw():
    background(200) # fundo cinza claro
    rectMode(CENTER) # retângulos desenhados pelo centro
    stroke(0) # linha em preto
    strokeWeight(2) # espessura de linha 2px
    noFill()  # sem preenchimento

    grid_elem = int(input.analog(1) / 16)  # 0 a 64, número de linhas e colunas na grade
    elem_size = int(input.analog(2) / 16)  # 0 a 64, tamanho base de cada quadrado
    rand_size = int(input.analog(3) / 16)  # 0 a 64, ativa faixa entre -64 e 63 para randomizar tamanho
    rand_posi = int(input.analog(4) / 16)  # 0 a 64, ativa faixa equivalente para randomizar a posição

    randomSeed(int(input.analog(1))/4) # trava a randomização entre os ciclos de draw
    spac_size = int(width / (grid_elem + 1)) # calcula o espaçamento entre os quadrandos
    for x in range(spac_size / 2, width , spac_size):     # para cada coluna um x
        for y in range(spac_size / 2, width , spac_size): # para cada linha um y
            square_size = elem_size + rand_size * random(-1, 1) # sorteia um tamanho (se o rand_size > 0)
            rect(x + rand_posi * random(-1, 1),  # desenha um quadrado
                 y + rand_posi * random(-1, 1),  
                 square_size,
                 square_size)

    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 20 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    input.update()


def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()

    input.keyPressed()

def keyReleased():
    input.keyReleased()
