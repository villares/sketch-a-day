"""
Black and White pattern

Code for py5 (py5coding.org) module mode


"""

import py5
import numpy as np
#from decimal import Decimal

p = 5 #Decimal('3')

def setup():
    global w, h, img
    py5.size(600, 600)
    py5.no_smooth()
    w, h = py5.width // 4, py5.height // 4
    img = py5.create_image(w, h, py5.ALPHA)

@np.vectorize
def pattern(x, y):
    return 0 if (y ^ x) ** (p / 10) % 256 < 32 else 255

def draw():
    xg, yg = np.mgrid[0:w, 0:h]
    dg = pattern(xg, yg)
    py5.create_image_from_numpy(dg, 'L', dst=img)
    py5.image(img, 0, 0, py5.width, py5.height)

def key_pressed():
    global p
    if py5.key == 'a':
        p += 1 #Decimal('0.1')
    elif py5.key == 'z' and p > 1:
        p -= 1 #Decimal('0.1')
    print(p)

py5.run_sketch(block=False)
