
from __future__ import division
from itertools import product
from random import randint

h_sin_rnd = lambda x, y, w, h: random(2) < 1 + sin(x / w * TWO_PI)
v_sin_rnd = lambda x, y, w, h: random(2) < 1 + sin((y / h) * TWO_PI)    


def setup():
    size(512 + 256 + 128, 512 + 256 + 128)
    background(128)
    grid(0, 0, width)
   
def grid(xo, yo, w):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 16 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                stroke(0, 0, 100)
                region(x, y, qw, qw, h_sin_rnd)
            else:
                stroke(0, 100, 0)
                region(x, y, qw, qw, v_sin_rnd)

def region(xo, yo, w, h, rule):
    grid = product(range(xo, xo + w), range(yo, yo + h))
    for x, y in grid:
        if rule(x - xo, y - yo, w, h):
            point(x, y)
            
