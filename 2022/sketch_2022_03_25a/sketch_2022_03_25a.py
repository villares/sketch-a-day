from random import shuffle, sample
from itertools import product

def setup():
    global elements
    size(800, 800)
    elements = prepare_elements(3)
    
def prepare_elements(n):
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
            if tw / w < 5 and th / h  <  5 and n > 0:
                elements.append((x, y, w, h, tw, th, prepare_elements(n - 1)))
            else:
                elements.append((x, y, w, h, tw, th, []))
            x += w
        y += h
    return elements
    
def draw():
    draw_elements(elements, 0, 0, width, height)
    
def draw_elements(elements, x0, y0, tw, th):
    for x, y, w, h, etw, eth, sub in elements:
        xf = tw / etw
        yf = th / eth
        if not sub:
            fill(w * 10, 200, h * 10)
            rect(x0 + x * xf, y0 + y * yf, w * xf, h * yf)
        else:
            draw_elements(sub, x0 + x * xf, y0 + y * yf, w * xf, h * yf)

def key_pressed():
    global elements
    elements = prepare_elements(3)
    