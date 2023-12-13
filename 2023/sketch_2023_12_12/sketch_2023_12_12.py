# module mode
import py5
from collections import deque

pontos =  deque(maxlen=500) # lista vazia global

def setup():
    py5.size(800, 800)
    py5.no_fill()

def draw():
    py5.background(250, 250, 200)
    for i, (x, y) in enumerate(pontos):
        xm, ym = pontos[py5.frame_count % len(pontos)]
        d = 10 * py5.sqrt(1 + py5.dist(x, y, xm + 5, ym + 5))
        #py5.stroke_weight(60 / d)
        py5.circle(x, y, d)

def mouse_dragged():
    pontos.append((py5.mouse_x, py5.mouse_y))  # note a tupla!

def key_pressed():
    pontos.clear()

py5.run_sketch()  