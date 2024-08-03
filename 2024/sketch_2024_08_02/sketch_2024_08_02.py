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
        py5.stroke(128)
        py5.square(0, 0, ext)
        py5.stroke(255)
        ax, ay, bx, by = 0, ext/2, ext * TAN_A, -ext/2
        py5.line(ax, ay, bx, by)
        py5.line(ax, -ay, bx, -by)
        py5.line(-ax, ay, -bx, by)
        py5.line(-ax, -ay, -bx, -by)
        py5.line(ay, -ax, by, -bx)
        py5.line(-ay, -ax, -by, -bx)
        py5.line(ay, ax, by, bx)
        py5.line(-ay, ax, -by, bx)

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)