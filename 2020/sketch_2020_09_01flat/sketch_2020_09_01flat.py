from bezmerizing import Polyline, Path
#from flat import document, shape, rgb, rgba, command, path
from random import choice, randint
from flat_processing import *

import os
os.chdir(os.path.dirname(__file__))

def setup():
    size(800, 800)
    background(200)
    fill(0, 0, 200, 100)
    grid(400, 400., 5, 150, ensamble, 5) # ensamble of 5 , on grid also order=5
    # grid(width/4.*3, height/2., 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5
    page.image(ppi=92, kind="rgb").png(__file__[-24:-3]+'.png')
    page.svg(__file__[-24:-3]+'.svg')
    # d.pdf("sketch.pdf")
    #page.image(ppi=92, kind="rgb").png("sketch_2020_08_29.png")

def ensamble(ex, ey, order):
    for _ in range(order):
        order, spacing, side = randint(3, 5), 14, 7
        x, y = randint(-5, 4) * side, randint(-5, 4) * side   
        grid(ex+x, ey+y, order, spacing, choice(gliphs), side)


def grid(x, y, order, spacing, function, *args):
    xo, yo = (x - order * spacing / 2, y - order * spacing / 2)
    for i in range(order):
        gx = spacing/2 + i * spacing
        for j in range(order):
            gy = spacing/2 + j * spacing
            function(xo + gx, yo + gy, *args)

gliphs = [lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
          ]


setup()
