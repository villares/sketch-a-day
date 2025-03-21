# module mode
import py5
from collections import deque

pontos =  deque(maxlen=500) # lista vazia global

def setup():
    py5.size(800, 800)    

def draw():
    py5.background(0, 0, 100)
    for i, (x, y) in enumerate(pontos):
        d = 40 + 30 * py5.sin((i + py5.frame_count) / 10)
        py5.circle(x, y, d)

def mouse_dragged():
    pontos.append((py5.mouse_x, py5.mouse_y))  # note a tupla!

def key_pressed():
    pontos.clear()

py5.run_sketch()  