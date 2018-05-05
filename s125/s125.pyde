# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s125"  # 180505

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT, ELEMENTS
    size(600, 600)
    rectMode(CENTER)  # retângulos desenhados pelo centro
    noFill()  # sem contorno
    frameRate(30)
    strokeWeight(3)
    ELEMENTS = []
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2])
    create_grid()

def draw():
    background(127)  # fundo cinza claro

    for stroke_c, x, y, el_size, status in ELEMENTS:
        if dist(x, y, mouseX, mouseY) < spac_size * 2:
            fill(0, 100)
        else:
            noFill()
        if status:
            stroke(stroke_c)
            pointy_hexagon(x, y, el_size)

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
    if keyCode == SHIFT:
        create_grid()

    input.keyPressed()

def keyReleased():
    input.keyReleased()

def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]

def item_at_x_y(x, y, collenction, width_):
    return collection[x + y * width_]

def pointy_hexagon(x, y, r):
    with pushMatrix():
        translate(x, y)
        rotate(radians(30))  # pointy, comment out for "flat_hexagon()"
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6) * r
            sy = sin(i * TWO_PI / 6) * r
            vertex(sx, sy)
        endShape(CLOSE)

def create_grid():
    global grid_elem, rand_size, spac_size
    # seize inputs
    grid_elem = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    rand_size = int(input.analog(2) / 16)  # escala a randomização do tamanho
    randomSeed(int(input.analog(1)) / 4)
    # espaçamento entre os elementos
    spac_size = int(width / (grid_elem + 0.01))

    # empty list
    ELEMENTS[:] = []
    v = spac_size * 1.5
    h = spac_size * sqrt(3)
    for _ in range(1):
        for ix in range(grid_elem):  # um x p/ cada coluna
            # um y p/ cada linha
            for iy in range(grid_elem):
                if iy % 2:
                    x = ix * h + h / 4
                else:
                    x = ix * h - h / 4
                y = iy * v
                final_size = spac_size + rand_size * random(-1, 1)
                C = map(final_size, 0, 63, 0, 255)
                ELEMENTS.append((C, x, y, final_size, int(random(2))))
