from __future__ import division
from random import choice

def setup():
    size(600, 600)
    noLoop()
    # strokeJoin(ROUND)
    # blendMode(MULTIPLY)
    colorMode(HSB)
    rectMode(CENTER)

def draw():
    global c
    c = 0
    background(0)
    grid(width / 2, width / 2, 4, width)

def grid(xo, yo, n, tw, e=None):
    global c
    c += 1
    """
    Faça o desenho do grid baseado em uma subdivisão (grade) recursiva
    """
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            if cw > 20 and random(10) < 8: # faz subdivisão recursiva
                grid(x, y, 3, cw) 
            else:  # faz um elemento "sozinho"
                fill(c * 1.5 % 256, 200, 200)
                rect(x, y, cw, cw, i * 5, j * 5, i * 5, j * 5)





def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
