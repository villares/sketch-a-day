# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org


import py5
import numpy as np
from cmath import log as clog
from cmath import exp as cexp

def setup():
    py5.size(600, 600)
    W = 300
    pts = []
    for x in range(-W, W, 10):
        for y in range(-W, W, 2):
            pts.append((x, y))
    for y in range(-W, W, 10):
        for x in range(-W, W, 2):
            pts.append((x, y))
    global xy_pts
    xy_pts =  np.array(pts)

def draw():
    py5.translate(300, 300)
    py5.background(0)
    py5.stroke(128)
    py5.points(xy_pts)

    c_pts = xy_pts[:, 0] + 1j * xy_pts[:, 1]
    non_zero = c_pts != 0
    c_log = np.zeros_like(c_pts, dtype=complex)
    c_log[non_zero] = np.log(c_pts[non_zero])
    log_xy_pts = np.column_stack((c_log.real, c_log.imag))
    
    py5.stroke(0, 255, 0)
    py5.points(log_xy_pts * 90 - (300, 0))

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)

