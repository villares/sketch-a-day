from itertools import product

import py5

A = py5.radians(45 / 2)
TAN_A = py5.tan(A)

def setup():
    py5.size(600, 600)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()

def draw():
    py5.background(100)
    for x, y in product(range(100, 501, 200), repeat=2):
        module(x, y, 200)
    
def module(x, y, ext):
    with py5.push_matrix():
        py5.translate(x, y)
        #py5.stroke(128)
        #py5.square(0, 0, ext)
        py5.stroke(255)
        ax, ay, bx, by = 0, ext/2, ext * TAN_A, -ext/2
        gap_line(ax, ay, bx, by)
        gap_line(ax, -ay, bx, -by, -1)
        gap_line(ax, -ay, bx, -by, -1)
        gap_line(-ax, ay, -bx, by, -1)
        gap_line(-ax, -ay, -bx, -by)
        gap_line(ay, -ax, by, -bx)
        gap_line(-ay, -ax, -by, -bx, -1)
        gap_line(ay, ax, by, bx, -1)
        gap_line(-ay, ax, -by, bx)

def m(a, b):
    return (a + b) / 2

def rot(x, y, cw=1, ang=None):  
    ang = ang or -A * 2 # -45 degrees by default for this sketch
    return  (x * py5.cos(ang * cw) + y * py5.sin(ang * cw),
            -x * py5.sin(ang * cw) + y * py5.cos(ang * cw))

def gap_line(ax, ay, bx, by, cw=1):
    #py5.line(ax, ay, bx, by)
    mx, my = m(ax, bx), m(ay, by)
    py5.line(mx, my, bx, by)
    rx, ry = rot(mx, my, cw) # not always clockwise :/
    #py5.circle(rx, ry, 5)
    py5.line(ax, ay, rx, ry)

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)