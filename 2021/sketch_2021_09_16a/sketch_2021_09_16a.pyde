from __future__ import division
from itertools import product

def setup():
    size(500, 500)
    background(128)
    stroke(0, 0, 100)
    h_sin_rnd = lambda x, y, w, h: random(2) < 1 + sin(x / w * TWO_PI)
    region(50, 000, 400, 500, h_sin_rnd)
    stroke(0, 100, 0)
    v_sin_rnd = lambda x, y, w, h: random(2) < 1 + sin((y / h) * TWO_PI)    
    region(0, 50, 500, 400, v_sin_rnd)


def region(xo, yo, w, h, rule):
    grid = product(range(xo, xo + w), range(yo, yo + h))
    for x, y in grid:
        if rule(x - xo, y - yo, w, h):
            point(x, y)
            
    
                
