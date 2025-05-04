# inspired by Marius Watz's work...

import py5
from py5 import sin, cos, radians, PI, TAU

def setup():
    py5.size(600, 600, py5.P3D)
    py5.color_mode(py5.HSB)
    
def draw():
    py5.background(0)
    py5.no_stroke()
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_y(radians(py5.mouse_x))
    for i in range(6):
        py5.rotate_y(TAU / 3)
        for j in range(6):
            py5.rotate_z(TAU / 4)
            for k in range(6):
                py5.rotate_x(TAU / 5)
                py5.fill(j * 16, 200, 255, 100)
                if j % 2 == 1 and k % 3 == 0 and i % 3 == 0:
                    py5.fill(255, 200)
                if j % 2 == 0:
                    spaced_arc(0, 0, 60,
                           50 + 25 * i - 25 * k, 25)            
                else:
                    solid_arc(0, 0, 60,
                           50 + 25 * i - 25 * k, 10)                    

def solid_arc(x, y, deg, rad, w):
    vs = []
    for i in range(0, deg, 5):
        a = radians(i)
        vs.extend((
            (cos(a) * (rad) + x,
             sin(a) * (rad) + y),
            (cos(a) * (rad + w) + x,
             sin(a) * (rad + w) + y)))
    py5.begin_shape(py5.QUAD_STRIP)
    py5.vertices(vs)
    py5.end_shape()

def spaced_arc(x, y, deg, rad, w, s=6, t=3):
    vs = []
    for i in range(0, deg, s):
        a = radians(i)
        b = radians(i + t)
        vs.extend((
            (cos(a) * (rad) + x,
             sin(a) * (rad) + y),
            (cos(a) * (rad + w) + x,
             sin(a) * (rad + w) + y),
            (cos(b) * (rad + w) + x,
             sin(b) * (rad + w) + y),
            (cos(b) * (rad) + x,
             sin(b) * (rad) + y),            
            ))
    py5.begin_shape(py5.QUADS)
    py5.vertices(vs)
    py5.end_shape()

py5.run_sketch(block=False)
