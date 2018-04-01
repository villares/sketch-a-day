# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s090"  # 180331

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider
from shapes import *

A = Slider(1, 40, 10, 'q', 'a')
B = Slider(1, 100, 50, 'w', 's')
C = Slider(1, 40, 20, 'e', 'd')
D = Slider(1, 40, 10, 'r', 'f')

SHAPES = [circle,
          square,
          exes,
          losang]

def setup():
    size(600, 600, P2D)
    # rectMode(CENTER) # forgot this and it dislocates losangs :(
    # but now I've left like this for this one :)    
    
    A.position(40, height - 70)
    B.position(40, height - 30)
    C.position(width - 140, height - 70)
    D.position(width - 140, height - 30)

def draw():
    background(200)

    a = int(A.val)  # number of elements
    b = C.val * B.val / 100  # size of el ements (B.val % of spacing!)
    c = int(C.val)  # spacing between elements
    d = int(D.val)  # number of grids

    randomSeed(100)  # a different random seed

    for i in range(d):
        tam = a * c
        x = int(random(c, width - tam) / c) * c
        y = int(random(c, height - tam) / c) * c
        #random_a = rnd_choice(range(1, a + 1))
        grid(x, y,  # random starting point
             a,  # number of elements
             b,         # size of elements, a B.val percentage of C.val
             c,                   # spacing of grid elements
             rnd_choice(SHAPES))  # random shape drawing function

    # uncomment next lines to export GIF
    if not frameCount % 30:
         gif_export(GifMaker,
                    frames=2000,
                    delay=500,
                    filename=SKETCH_NAME)

    # Draws sliders and checks for mouse dragging or keystrokes
    Slider.update_all()

def grid(x, y, num, size_, space, func):
    for i in range(x, x + num * space, space):
        strokeWeight(2)
        stroke(rnd_choice(COLORS))
        noFill()
        for j in range(y, y + num * space, space):
            func(i, j, size_)

def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
