import py5
from math import sin, cos, pi
from itertools import product
from random import randint, random

hor = lambda x, y, w, h: 5 + 5 * cos (y / pi) < 5 - 5 * cos(x / w * 2 * pi)
ver = lambda x, y, w, h: 5 + 5 * cos (x / pi) < 5 - 5 * cos(y / h * 2 * pi)    

def setup():
    py5.size(960, 960)
    py5.background(32)
    py5.scale(0.25)
    grid(0, 0, py5.width * 4)
    # py5.saveFrame('sketch_2021_09_19b.png')
   
def grid(xo, yo, w):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 64 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                py5.stroke(200, 0, 0)
                region(x, y, qw, qw, hor)
            else:
                py5.stroke(200)
                region(x, y, qw, qw, ver)

def region(xo, yo, w, h, rule):
    for x, y in product(range(xo, xo + w), range(yo, yo + h)):
        if rule(x - xo, y - yo, w, h):
            py5.point(x, y)
            
py5.run_sketch()