import py5
from random import shuffle, sample, seed
from itertools import product

RECURSION_LEVELS = 2

def setup():
    global elements
    py5.size(600, 600, py5.P3D)
    py5.stroke(0, 32)
    elements = prepare_elements(RECURSION_LEVELS)

def prepare_elements(n):
#    ns = (16, 16, 8, 16, 8, 8, 32, 32)
    ns = (1, 1, 2, 3, 5, 8, 13, 21)
    ws = sample(ns, 5)
    shuffle(ws)
    hs = sample(ns, 5)
    shuffle(hs)
    elements = []
    tw = sum(ws)
    th = sum(hs)
    y = 0
    for h in hs:
        x = 0
        for w in ws:
            if tw / w < 5 and th / h < 5 and n > 0:
                elements.append((x, y, w, h, tw, th, prepare_elements(n - 1)))
            else:
                elements.append((x, y, w, h, tw, th, []))
            x += w
        y += h
    return elements

def draw():
    py5.background(60, 60, 100)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_x(py5.QUARTER_PI)
    py5.rotate_z(py5.QUARTER_PI)
    py5.translate(-py5.width / 2, -py5.height / 2, 0)    
    draw_elements(elements, 0, 0, py5.width, py5.height)

def draw_elements(elements, x0, y0, tw, th):
    for x, y, w, h, etw, eth, sub in elements:
        xf = tw / etw
        yf = th / eth
        py5.fill(w * 10, 200, h * 10)
        d =  0.5 * (w * xf * h * yf) ** 0.5
        py5.push()
        slab(x0 + x * xf, y0 + y * yf, 0,
             w * xf, h * yf, d)
        py5.translate(0, 0, d)
        if sub:
            draw_elements(sub, x0 + x * xf, y0 + y * yf, w * xf, h * yf)
        py5.pop()

def slab(x, y, z,  w, h, d):
    py5.push()
    py5.translate(x + w / 2, y + h / 2, z + d / 2)
    py5.box(w, h, d)
    py5.pop()

def key_pressed():
    global elements
    elements = prepare_elements(RECURSION_LEVELS)
    m = py5.millis()
    seed(m)
    print(m)

py5.run_sketch()
