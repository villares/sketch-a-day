import numpy as np
import py5

def setup():
    py5.size(400, 400)
    py5.stroke_weight(4)
    dotted_line(100, 100, 300, 300, d=16)
    dotted_line(100, 100, 300, 100, d=8)
    dotted_line(100, 300, 300, 300, d=8)

def dotted_line(*args, d=5):
    # d is the aprox. distance between dots
    ax, ay, bx, by = args
    a = np.array((ax, ay))
    b = np.array((bx, by))
    line_len = py5.dist(ax, ay, bx, by)
    n = int(line_len / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    py5.points(coords)

def key_pressed():
    py5.save_frame(f'out.png')
  
py5.run_sketch()