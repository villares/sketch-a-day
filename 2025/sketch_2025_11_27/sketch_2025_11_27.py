# This code is an example of py5 in module mode, learn more at <py5coding.org>

import py5
import numpy as np

w = 0

def setup():
    global ns, ys
    py5.size(600, 600)
    py5.stroke_cap(py5.PROJECT)
    py5.stroke(0, 64)
    py5.no_loop()

def draw():
    py5.background(240)
    step = 0.01
    xs = np.arange(600)
    pts = []
    for j in range(10):
        for i in range(10):
            ns = py5.os_noise(
                xs * step,
                5 * i * step,
                5 * j * step,
                w * step
                )
            ys = ns * 100 + i * 60
            pts.extend(np.array((xs, ys)).T)
    py5.points(pts)
    
def key_pressed():
    global w
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == 'a':
        w += 1
    elif py5.key == 'z':
        w -= 1
    py5.redraw()
    
py5.run_sketch(block=False)
