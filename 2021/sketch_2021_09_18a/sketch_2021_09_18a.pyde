
from __future__ import division
from itertools import product
from random import randint

hor = lambda x, y, w, h: random(0, 2.5) < 1 + sin(x / w * TWO_PI)
ver = lambda x, y, w, h: random(0, 2.5) < 1 + sin(y / h * TWO_PI)    

def setup():
    size(960, 960)
    scale(0.5)
    strokeWeight(1.5)
    # noSmooth()
    #size(512 + 256 + 128, 512 + 256 + 128)
    background(32)
    grid(0, 0, width * 2)
    # saveFrame('sketch_2021_09_18b.png')
   
def grid(xo, yo, w):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 32 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                stroke(0, 100, 200); stroke(200)
                region(x, y, qw, qw, hor)
            else:
                stroke(100, 0, 200)#; stroke(100)
                region(x, y, qw, qw, ver)

def region(xo, yo, w, h, rule):
    grid = product(range(xo, xo + w), range(yo, yo + h))
    for x, y in grid:
        if rule(x - xo, y - yo, w, h):
            point(x, y)
            
