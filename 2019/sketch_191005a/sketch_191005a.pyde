from random import choice
from elementos import casinha, estrela
def setup():
    size(780, 780)
    noLoop()
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(255)
    grade(width / 2, width / 2, 4, width)

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
                grade(x, y, 3, cw * 2, 1 + o)
            else:
                fill(0)
                element(x, y, cw, o)


def element(x, y, w, option):
    stroke(0)
    strokeWeight(1)
    if option == 0:
        p = choice((3, 5, 7))
        estrela(x, y, p, choice((w/6, w*.1, w*.2)), w/3)
    else:
        # casinha(x, y, choice((w/2, w*.9, w*.6)))
        casinha(x, y, w)



def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
