from __future__ import division
from itertools import product

def setup():
    size(600, 600)
    background(240)
    grid = product(range(width), range(height))
    map(element, grid)
    
def element(pos):
    x, y = pos
    d = dist(x, y, width / 2, height / 2)
    a = sin(sqrt(d) * 2) + 1  # concentric waves
    b = sin(y / 50 + x / 100) + 1  # diagonal bands
    if random(4) > a + b:
        point(x, y)
    
