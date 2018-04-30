# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s118"  # 180428

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

ELEMENTS, BUFFER = [], []
GIF_EXPORT = False

def setup():
    global input
    size(600, 600)
    noFill()  # sem preenchimento
    frameRate(30)
    strokeWeight(3)
    colorMode(HSB)
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2, 3, 4])

def draw():
    background(0)
    
    grid_elem = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    elem_size = int(input.analog(2) / 16)  # 0 a 63 tamanho base dos quadrados
    rotation = int(input.analog(3) / 16)  # escala a randomização do tamanho
    rand_posi = int(input.analog(4) / 16)  # escala a randomização da posição
    # trava a random entre os ciclos de draw
    # mas varia com o número de colunas na grade
    randomSeed(int(input.analog(1)) / 4)
    # espaçamento entre os elementos
    spac_size = width / (grid_elem + 1)
    v = spac_size * 1.5
    h = spac_size * sqrt(3)
    for ix in range(-1, grid_elem + 1):
        for iy in range(-1, grid_elem + 1):
            if iy % 2:
                x = ix * h + h / 4
            else:
                x = ix * h - h / 4
            y = iy * v
            for i in range(2):
                final_size = spac_size - i * 0.5 * elem_size
                oX = rand_posi * random(-1, 1)
                oY = rand_posi * random(-1, 1)
                ELEMENTS.append((x + oX, y + oY, final_size))

    for e0, e1 in zip(ELEMENTS[0::2], ELEMENTS[1::2]):
        x0, y0, es0 = e0
        x1, y1, es1 = e1
        for i in range(5):
            x, y = lerp(x0, x1, .25 * i), lerp(y0, y1, .25 * i)
            fs = lerp(es0, es1, .25 * i)
            st = (lerp(0, 255, .25 * i) + frameCount) % 256
            with pushMatrix():
                translate(x, y)
                rotate(radians(10)*rotation)
                stroke(st, 255, 255)
                hexagon(0, 0, fs)

    # empty list
    ELEMENTS[:] = []

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

def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]

def hexagon(x, y, r):
    with pushMatrix():
        translate(x, y)
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6) * r
            sy = sin(i * TWO_PI / 6) * r
            vertex(sx, sy)
        endShape(CLOSE)
