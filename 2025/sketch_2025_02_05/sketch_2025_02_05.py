from itertools import chain

import py5
from py5 import sin, cos, TAU
import numpy as np

def setup():
    global pts, z
    py5.size(800, 400)
    py5.background(150)
    py5.no_fill()
    py5.stroke_weight(2)
    py5.stroke_join(py5.ROUND)
    py5.stroke(255)
    xc, yc = 200, 200
    for n in range(3, 8):
        pts = np.array(star_points(xc, yc, 45, 180, n))
        with py5.begin_closed_shape():
            py5.vertices(pts)
        for xa, ya in pts:
            dotted_line(xa, ya, xc, yc)
        xc += 100


def star_points(xc, yc, ra, rb, n):
    ang = TAU / n
    result = []
    for i in range(n):
        xa = xc + ra * cos(i * ang)
        ya = yc + ra * sin(i * ang)
        result.append((xa, ya))
        xb = xc + rb * cos(i * ang + ang / 2)
        yb = yc + rb * sin(i * ang + ang / 2)
        result.append((xb, yb))
    return result

def dotted_line(ax, ay, bx, by, d=5):
    a = np.array((ax, ay))
    b = np.array((bx, by))
    c = py5.dist(ax, ay, bx, by)
    n = int(c / d)
    t = np.linspace((0, 0,), (1, 1), n)
    coords = py5.lerp(a, b, t)
    py5.points(coords)

def key_pressed():
    py5.save_frame('out###.png')
    
py5.run_sketch(block=False)
