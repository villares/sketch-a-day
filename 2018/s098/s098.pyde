# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s098"  # 180408

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    size(600, 600)
    colorMode(HSB)
    rectMode(CENTER)  # retângulos desenhados pelo centro
    noStroke()  # sem contorno
    frameRate(30)
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino)

def draw():
    background(0)  # fundo cinza claro

    grid_elem = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    elem_size = int(input.analog(2) / 16)  # 0 a 63 tamanho base dos quadrados
    rand_size = int(input.analog(3) / 16)  # escala a randomização do tamanho
    rand_posi = int(input.analog(4) / 16)  # escala a randomização da posição
    # trava a random entre os ciclos de draw
    # mas varia com o número de colunas na grade
    randomSeed(int(input.analog(1)) / 4)
    # espaçamento entre os quadrandos
    spac_size = int(width / (grid_elem + 1))
    for x in range(spac_size / 2, width, spac_size):  # um x p/ cada coluna
        for y in range(spac_size / 2, width, spac_size):  # um y p/ cada linha
            # sorteia um tamanho (se o rand_size > 0)
            square_size = elem_size + rand_size * random(-1, 1)
            offsetX = rand_posi * random(-1, 1)
            offsetY = rand_posi * random(-1, 1)
            HUE = map(offsetX + offsetY, -128, 127, 0, 255)
            SAT = map(square_size, 0, 63, 0, 255)
            fill(HUE, SAT, 255, 200)
            rect(x + offsetX,  # desenha um quadrado
                 y + offsetY,
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
