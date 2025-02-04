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
    py5.stroke(255)
    xc, yc = 200, 200
    n = 6
    pts = np.array(star_points(xc, yc, 160, 90, n))
    with py5.begin_closed_shape():
        py5.vertices(pts)
    line_pts = list(chain(*zip(pts, [(xc, yc)] * n * 2)))
    with py5.begin_shape(py5.LINES):
        py5.vertices(line_pts)
    translated_pts = pts + np.array((400, 0))
    smaller_pts = (pts - np.array((xc, yc))) / 5
    for x, y in translated_pts:
        with py5.push_matrix(), py5.begin_closed_shape():
            py5.translate(x, y)
            py5.vertices(smaller_pts)


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

def key_pressed():
    py5.save_frame('out###.png')
    
py5.run_sketch(block=False)
