from random import sample
from bezmerizing import Polyline, Path
#from flat import document, shape, rgb, rgba, command, path
from flat_processing import *

from random import choice
from random import randint

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


fill(0, 0, 200)
grid(400, 400., 5, 150, ensamble, 5) # ensamble of 5 , on grid also order=5
# grid(width/4.*3, height/2., 4, 150, ensamble, 5) # ensamble of 5 , on grid also order=5


# background(0, 200, 0)


d.pdf("test2.pdf")
page.svg('test2.svg')
#page.image(ppi=92, kind="rgb").png("sketch_2020_08_29.png")