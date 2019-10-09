from random import choice
from elementos import casinha, estrela, poly_arrow

def setup():
    size(780, 780)
    noLoop()
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(255)
    grade(width / 2., width / 2., 4, width)

def grade(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = (i + j) % 10
            noFill()
            if e is not None:
                element(x, y, cw, e)
            elif cw > 40 and random(10) < 8:
                grade(x, y, 3, cw)
            elif cw > 20 and random(10) < 8:
                grade(x, y, 3, cw * 1.5, 1 + o)
            else:
                fill(0)
                element(x, y, cw, o)


def element(x, y, w, option):
    stroke(0)
    strokeWeight(1)
    p = choice((0, 1, 2))
    pushMatrix()
    translate(x, y)
    rotate(HALF_PI * p)
    if option == 0:
        poly_arrow(0, 0, w)
        # estrela(x, y, p, choice((w/6, w*.1, w*.2)), w/3)
    else:
        # casinha(x, y, choice((w/2, w*.9, w*.6)))
        poly_arrow(0, 0, w)
    popMatrix()

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
