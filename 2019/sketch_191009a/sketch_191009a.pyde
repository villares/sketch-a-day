from random import choice
from elementos import casinha, estrela, poly_arrow

def setup():
    size(768, 768)
    noLoop()
    colorMode(HSB)
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(255)
    grade(width / 2., width / 2., 4, width)

def grade(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = 1 + (i + j * 2) % 8
            noFill()
            if e is not None:
                element(x, y, cw, e)
            elif cw > 10 and random(10) < 6:
                grade(x, y, 4, cw)
            elif cw > 20 and random(10) < 6:
                grade(x, y, 2, cw + 1, 0)
            else:
                element(x, y, cw, o)


def element(x, y, w, option):
    stroke(0)
    strokeWeight(1)
    p = choice((0, 1, 2))
    pushMatrix()
    translate(x, y)
    rotate(HALF_PI * p)
    if option == 0:
        fill(0)
        poly_arrow(0, 0, w)
        # estrela(x, y, p, choice((w/6, w*.1, w*.2)), w/3)
    else:
        # casinha(x, y, choice((w/2, w*.9, w*.6)))
        # fill(option * 32, 200, 200)
        fill(option * 8, 100)
        noStroke()
        poly_arrow(0, 0, w * 1.5)
    popMatrix()

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
