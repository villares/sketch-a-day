from __future__ import division
from itertools import product

ca = color(100, 50, 0)
cb = color(50, 0, 255)

def setup():
    size(1200, 600)
    background(240)
    grid = product(range(600), range(height))
    map(element, grid)
    grid = product(range(600, 1200), range(height))
    colorMode(HSB)  # MESSING UP THE lerpColor!
    map(element, grid)
     
def element(pos):
    x, y = pos
    d = dist(x, y, 600, height / 2)
    a = sin(sqrt(d) * 2) + 1  # concentric waves
    b = sin(y / 50 + x / 100) + 1  # diagonal bands
    c = lerpColor(ca, cb, (a + b) / 4)
    set(x, y, c)
    
