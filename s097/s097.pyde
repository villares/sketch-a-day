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
    background(200)
    rectMode(CENTER)
    stroke(0)
    #noStroke()
    strokeWeight(2)
    #fill(255, 100)
    noFill()

    grid_elem = int(input.analog(1) / 16)  # 0 to 64
    elem_size = int(input.analog(2) / 16)  # 0 to 64
    rand_size = int(input.analog(3) / 16)  # 0 to 64
    rand_posi = int(input.analog(4) / 16)  # 0 to 64
    #print(grid_size, elem_size, spac_size, rand_range)
    randomSeed(int(input.analog(1))/4)
    spac_size = int(width / (grid_elem + 1))
    for x in range(spac_size / 2, width , spac_size):
        for y in range(spac_size / 2, width , spac_size):
            square_size = elem_size + rand_size * random(-1, 1)
            rect(x + rand_posi * random(-1, 1),
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
