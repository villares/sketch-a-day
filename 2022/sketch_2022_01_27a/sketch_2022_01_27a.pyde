from __future__ import division
from itertools import product
from villares.helpers import hex_color

colors = (
    "2E294E",
    "F1E9DA",
    "541388",
    "FFD400",
    "D90368"
    )

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
    c = hex_color(colors[int(a + b - 2.5)])
    set(x, y, c)
    
