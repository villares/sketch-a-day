from itertools import product

import numpy as np
import py5

grid_points = list(product(range(-350, 351, 25), repeat=2))

def setup():
    py5.size(800, 800)
    py5.no_stroke()
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    n = len(grid_points)
    w = np.linspace(5, 25, n)
    h = np.linspace(25, 5, n)
    angs = np.linspace(0, py5.TAU, n)
    rect_infos = zip(grid_points, w, h, angs)
    pts = list(map(draw_rect, rect_infos))
    #py5.points(pts)
    
def draw_rect(rect_info):
    pos, w, h, rot = rect_info
    b = py5.remap(rot, 0, py5.TAU, 0, 255)
    py5.fill(h * 10, abs(pos[1] / 2), b)
    with py5.push_matrix():
        py5.rect_mode(py5.CENTER)
        py5.translate(*pos)
        py5.rotate(rot)
        py5.rect(0, 0, w, h)
    return pos

def key_pressed():
    py5.save('out.png')
    
py5.run_sketch(block=False)