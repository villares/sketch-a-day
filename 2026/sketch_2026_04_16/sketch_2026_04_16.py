# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org


import py5
from cmath import log as clog
from cmath import exp as cexp

def setup():
    py5.size(600, 600)
    
def draw():
    py5.translate(300, 300)
    py5.background(0)
    pts = []
    for x in range(-600, 600, 10):
        for y in range(-600, 600, 2):
            pts.append((x, y))
    for y in range(-600, 600, 10):
        for x in range(-600, 600, 2):
            pts.append((x, y))
    py5.stroke(128)
    py5.points(pts)
    epts = []
    for x, y in pts:
        c = complex(x, y)
        ce = cexp(c) * 100
        epts.append((ce.real, ce.imag))
    py5.stroke(0, 0, 255)
    py5.points(epts)
    cpts = []
    for x, y in pts:
        c = complex(x, y)
        if c != 0:
            cl = clog(c) * 100 - 300
            cpts.append((cl.real, cl.imag))
    py5.stroke(0, 255, 0)
    py5.points(cpts)

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)

