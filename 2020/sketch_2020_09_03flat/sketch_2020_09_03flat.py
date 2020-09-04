from flask import Flask
from random import choice, randint
from flat_processing import *

def ensamble(ex, ey, eo):
    noStroke()
    for i in range(eo):
        if i % 2:
            fill(0, 0, 200, 100)
        else:
            fill(200, 0, 0, 100)
        order, spacing, side = randint(3, 6), 14, 7
        x, y = randint(-5, 4) * side, randint(-5, 4) * side   
        grid(ex+x, ey+y, order, spacing, choice(gliphs), side)


def grid(x, y, order, spacing, function, *args):
    if  type(order) is tuple:
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
    size(1500, 800)
    background(200)

    grid(width / 2, height / 2, (7, 5), 150, ensamble, 5) # ensamble of 5 , on grid also order=5
    # return page.svg()
    page.svg("test.svg")

if __name__ == '__main__':
    # app.run()
    draw()
    
    
  

