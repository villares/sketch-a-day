"""
My first glitch.com based sketch, visit https://sketch-2020-09-03a.glitch.me/ for new grids!
The base for this "glitch" is a fork of (@aparrish) Allison Parrish's amazing example using Flat + Bezmerizing to draw SVG.

I'm using a bizarre set of functions in flat_processing.py to make flat look like Processing Python mode I'm more used to.
"""

from flask import Flask
import random
from flat_processing import *

SEED = 1


def randint(a, b):
    return random.randint(a, b)

def choice(col):
    return col[int(randint(0, len(col)-1))]

def ensamble(ex, ey, eo):
    noStroke()
    for i in range(eo):
        if i % 2:
            fill(0, 0, 150, 150)
        else:
            fill(50, 150, 0, 150)
        order, spacing, side = randint(3, 6), 14, 7
        x, y = (1 + randint(-5, 4)) * side, (1 + randint(-5, 4)) * side
        grid(ex+x, ey+y, order, spacing, choice(gliphs), side)


def grid(x, y, order, spacing, function, *args):
    if type(order) is tuple:
        cols, rows = order
    else:
        cols = rows = order
    xo, yo = (x - cols * spacing / 2, y - rows * spacing / 2)
    for i in range(cols):
        gx = spacing/2 + i * spacing
        for j in range(rows):
            gy = spacing/2 + j * spacing
            function(xo + gx, yo + gy, *args)


gliphs = [lambda x, y, s: rect(x, y, s, s),
          lambda x, y, s: ellipse(x, y, s, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
          ]


# app = Flask(__name__)

# @app.route('/')
def draw():
    size(1400, 700)
    background(240)

    random.seed(SEED)

    grid(width / 2, height / 2, (8, 4), 150, ensamble, 5)
    return page.svg()


# draw()
# page.svg(__file__[-24:-3]+'-s{}.svg'.format(SEED))

if __name__ == '__main__':
    # app.run()
    draw()
    # page.svg(__file__[-24:-3]+f'-s{SEED}.svg')
    page.svg(__file__[-24:-3]+f'.svg')
