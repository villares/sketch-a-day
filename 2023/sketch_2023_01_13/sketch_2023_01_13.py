"""
SDF exploration

Code for py5 (py5coding.org) module mode
"""

import py5
import numpy as np

def setup():
    global HW, HH, img
    py5.size(600, 600)
    HW = py5.width / 2
    HH = py5.height / 2
    img = py5.create_image(600, 600, py5.ALPHA)

def L(x, y): return np.linalg.norm((x, y))  # return (x * x + y * y) ** 0.5

@np.vectorize
def vsdf(x, y, xo):
    ring = abs(L(x - 50, y - 50) - 100 + xo) - 50
    return min(y + 2 * xo, ring, x + 2 * xo)

def draw():
    py5.translate(HW, HH)
    xg, yg = np.mgrid[-300:300, -300:300]
    dg = vsdf(xg, yg, py5.mouse_x - HW)
    py5.create_image_from_numpy(dg, 'L', dst=img)
    py5.image(img, -HW, -HH)

py5.run_sketch()
