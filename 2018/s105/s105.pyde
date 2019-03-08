# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s105"  # 180415

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
#add_library('gifAnimation')

#from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT, ELEMENTS
    size(600, 600)
    noFill()  # sem contorno
    frameRate(30)
    strokeWeight(3)
    ELEMENTS = []
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2, 3, 4])

def draw():
    background(127)  # fundo cinza claro

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
            y = iy * v
            for i in range(3):
                final_size = elem_size * (i+0.5)
                C = map(final_size, 0, 63, 0, 255)
                ELEMENTS.append((C, x, y, final_size))
    # three layers of elements            
    for i in range(3):
        offsetX = rand_posi * random(-1, 1)
        offsetY = rand_posi * random(-1, 1)
        for elem in ELEMENTS[i::3]:
            st, x, y, es = elem
            fs = es + rand_size * random(-1, 1)
            stroke(st)
            ellipse(x + offsetX, y + offsetY, fs, fs)

    # for _ in range(grid_elem):
    #     stroke1, x1, y1, es1 = rnd_choice(ELEMENTS)
    #     stroke2, x2, y2, es2 = rnd_choice(ELEMENTS)
    #     #stroke(stroke1)
    #     line(x1, y1, x2, y2)

    # empty list
    ELEMENTS[:] = []

    # uncomment next lines to export GIF
    # global GIF_EXPORT
    # if not frameCount % 20 and GIF_EXPORT:
    #     GIF_EXPORT = gif_export(GifMaker,
    #                             frames=1000,
    #                             delay=300,
    #                             filename=SKETCH_NAME)

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
