from itertools import product

import numpy as np
import py5
from py5_tools import animated_gif

grid_points = list(product(range(-350, 351, 25), range(-150, 151, 25)))
n = len(grid_points)

def setup():
    global rects
    py5.size(800, 400)
    py5.no_stroke()
    w = np.linspace(5, 25, n)
    h = np.linspace(25, 5, n)
    angs = np.linspace(0, py5.TAU, n)
    rects = list(zip(grid_points, w, h, angs))
    animated_gif(
        'out.gif',
        duration=0.1,
        frame_numbers=range(1, 361, 5),
        optimize=False
    )
    
def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    f = py5.radians(py5.frame_count)
    for k, (pos, w, h, ang) in enumerate(rects):
        r = py5.remap(k, 0, n, 255, 0)
        g = abs(pos[1]) * 0.8 + 64 * py5.sin(f)
        b = py5.remap(k, 0, n, 0, 255)
        py5.fill(r, g, b)
        draw_rect(pos, w, h, ang + f)
        if k < n // 2:
            draw_rect(pos, w, h, ang + f + py5.PI/2)

def draw_rect(pos, w, h, rot):
    b = py5.remap(rot, 0, py5.TAU, 0, 255)
    with py5.push_matrix():
        py5.rect_mode(py5.CENTER)
        py5.translate(*pos)
        py5.rotate(rot)
        py5.rect(0, 0, w, h)
    return pos

def key_pressed():
    py5.save('out.png')
    
py5.run_sketch(block=False)

