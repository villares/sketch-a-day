from itertools import product

import numpy as np
import py5

TWO_PI = py5.TWO_PI

def setup():
    py5.size(1000, 1000)
    py5.stroke_weight(3)
    
def draw():
    py5.translate(512, 512)
    py5.background(0)
    N = 5
    for x, y in product(np.linspace(-py5.width/ 2, py5.width /2, 512), repeat=2):
        kx, ky =  kal(x, y, N)
        py5.stroke(
            128 + abs(kx) % 128,
            (kx + ky) % 255,
            255 - abs(ky) % 128)
        py5.point(x, y)
        #py5.point(x, y)

def kal(x, y, N):
    r, angle = py5.sqrt(x ** 2 + y ** 2), py5.atan2(y, x)
    angle = angle % TWO_PI
    angle += TWO_PI * (angle < 0) 
    theta = TWO_PI / (2 * N)
    slice_num = int(angle / theta)
    if slice_num % 2 == 1:
        angle = ((slice_num + 1) * theta) - angle
    else:
        angle -= slice_num * theta
    return r * py5.cos(angle), r * py5.sin(angle)

def key_pressed(): 
    py5.save_frame('out.png')

py5.run_sketch()