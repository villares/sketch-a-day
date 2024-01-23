from itertools import product

import py5, py5_tools
import numpy as np

fx = 300
fy = 300
pts = np.array(list(product(range(-150, 150), range(-150, 150))), dtype='float64')

def setup():    
    py5.size(400, 400)
    py5.stroke(255)
    py5.stroke_weight(3)
    py5_tools.animated_gif('out.gif', count=120, period=0.1, duration=0.1)

def draw():
    global fx, fy
    py5.background(0)
    py5.translate(200, 200)
    scaled_pts = pts.copy()
    spx = scaled_pts[:, 0]
    spy = scaled_pts[:, 1]
    spx *= fx
    spy *= fy
    py5.points(scaled_pts)
    
    if fx > 1:
        fx *= 0.9
    elif fy > 1:
        fy *= 0.9

py5.run_sketch()