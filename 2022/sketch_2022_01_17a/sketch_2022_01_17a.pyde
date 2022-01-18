from __future__ import division
from itertools import product

ca = color(100, 50, 0)
cb = color(50, 0, 255)

def setup():
    size(600, 600)
    background(240)
    grid = product(range(600), range(height))
    map(element, grid)

def element(pos):
    x, y = pos
    d = dist(x, y, 400, height / 2)
    a = sin(sqrt(d)* 3)  # concentric waves
    b = sin(y / 50 + x / 100)  # diagonal bands
    if  -0.66 < (a + b) < 0.66:
        c = color(0, 0, 200)
    elif (a + b) > 0:
        c = color(0)
    else:
        c = color(255)
    set(x, y, c)
    
