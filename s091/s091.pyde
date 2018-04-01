# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s091"  # 180401

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import gif_export
from shapes import *
from parameters import *

SHAPES = [circle,  # defined in shapes.py
          square,
          exes,
          losang]

aY, bY, cY, dY = 0, 0, 0, 0

def setup():
    size(600, 600)
    frameRate(30)
    background(0)
    global A, B, C, D
    # Ask user for Arduino port, cancel will return `None`
    port = Inputs.select_source(Arduino)
    # `None` will activate Sliders
    A, B, C, D = Inputs.setup_inputs(port)

def draw():
    global aY, bY, cY, dY
    # fill(0, 2)
    # rect(0, 0, width, height)

    a = A.val / 4
    b = B.val / 4
    c = C.val / 4
    d = D.val / 4
    noFill()
    stroke(255, 255, 255)
    ellipse(4 * width / 5, aY, a, a)
    stroke(0, 0, 255)
    ellipse(3 * width / 5, bY, b, b)
    stroke(0, 255, 0)
    ellipse(2 * width / 5, cY, c, c)
    stroke(255, 0, 0)
    ellipse(1 * width / 5, dY, d, d)

    if Inputs.TILT:
        background(0)

    # uncomment next lines to export GIF
    if not frameCount % 30:
         gif_export(GifMaker,
                    frames=2000,
                    delay=500,
                    filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    Inputs.update_inputs()

    aY += a / 16
    if aY > height + a:
        aY = -a

    bY += b / 16
    if bY > height + a:
        bY = -a

    cY += c / 16
    if cY > height + a:
        cY = -a

    dY += d / 16
    if dY > height + a:
        dY = -a


def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
