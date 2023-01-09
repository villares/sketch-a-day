"""
SDF exploration

Code for py5 (py5coding.org) imported mode
"""
from itertools import product
import numpy as np

def setup():
    global HW, HH
    size(600, 600)
    HW = width / 2
    HH = height / 2
    background(0)
    stroke_weight(3)
    color_mode(HSB, 360, 255, 255)

def L(x, y): return np.linalg.norm((x,y)) # return (x * x + y * y) ** 0.5

@np.vectorize
def vsdf(x, y, xo):
    ring = abs(L(x - 50, y - 50) - 100 + xo) - 50
    return min(y + xo, ring, x + xo), x, y

@np.vectorize
def vpoint(d, x, y):
    #if d < -3: stroke(0, 0, 200)
    #if d > 3: stroke(200, 0, 0)
    stroke(55 + d % 200, 255, 255)
    point(x, y)   

def draw():
    background(0)
    translate(HW, HH)
    xg, yg = np.mgrid[-500:500:5, -500:500:5]
    dg = vsdf(xg, yg, mouse_x - HW)
    vpoint(*dg)
    
#     for x, y in product(range(-500, 500, 5), repeat=2):
#         d = sdf(x, y)
#         stroke(55 + d % 200, 255, 255)
#         #if d < -3: stroke(0, 0, 200)
#         #if d > 3: stroke(200, 0, 0)
#         point(x, y)
    