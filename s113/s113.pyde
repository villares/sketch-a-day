# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s113"  # 180423 

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

ELEMENTS = []
GIF_EXPORT = False

def setup():
    global input
    size(600, 600)
    noStroke()  # sem traço
    frameRate(30)
    strokeWeight(3)
    colorMode(HSB)
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2, 3, 4])

def draw():
    background(0)  # fundo preto

    grid_elem = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    elem_size = int(input.analog(2) / 16)  # 0 a 63 tamanho base dos quadrados
    rand_size = int(input.analog(3) / 16)  # escala a randomização do tamanho
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
            if ix % 2:
                es = elem_size
            else:
                es = -elem_size
            y = iy * v
            for i in range(3):
                final_size = es * (i + 0.5)
                C = color(map(final_size, -100, 100, 0, 255),
                          255, 255, 100)
                oX = rand_posi * random(-1, 1)
                oY = rand_posi * random(-1, 1)
                ELEMENTS.append((C, x + oX, y + oY, final_size))
    # three layers of elements
    for e0, e1, e2 in zip(ELEMENTS[0::3], ELEMENTS[1::3], ELEMENTS[2::3]):
        st0, x0, y0, es0 = e0
        st1, x1, y1, es1 = e1
        st2, x2, y2, es2 = e2
        fs0 = es0 + rand_size * random(-1, 1)
        fs1 = es1 + rand_size * random(-1, 1)
        fs2 = es2 + rand_size * random(-1, 1)
        with pushMatrix():
            translate(x0,y0)
            rotate(fs0)
            fill(st0)
            hexagon(0, 0, fs0)
        with pushMatrix():
            translate(x1,y1)
            rotate(fs1)
            fill(st1)
            hexagon(0, 0, fs1)
        with pushMatrix():
            translate(x2,y2)
            rotate(fs2)
            fill(st2)
            hexagon(0, 0, fs2)

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
            sx = cos(i * TWO_PI /6) * r
            sy = sin(i * TWO_PI /6) * r
            vertex(sx, sy)
        endShape(CLOSE)
