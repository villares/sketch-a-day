from itertools import product

import numpy as np
import py5

grid_points = list(product(range(-380, 381, 21), range(-180, 181, 21)))
scale_factor = 5

def setup():
    global out
    py5.size(800, 400)
    n = len(grid_points)
    w = np.linspace(5, 20, n)
    h = np.linspace(20, 5, n)
    angs = np.linspace(0, py5.TAU, n)
    rect_infos = zip(grid_points, w, h, angs)
    out = py5.create_graphics(py5.width * scale_factor, py5.height * scale_factor)
    py5.begin_record(out)
    out.scale(scale_factor)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(0)
    py5.no_stroke()
    for ri in rect_infos:
        draw_rect(ri)
    py5.end_record()
    
def draw_rect(rect_info):
    pos, w, h, rot = rect_info
    b = py5.remap(rot, 0, py5.TAU, 0, 255)
    py5.fill(h * 10, abs(pos[1] / 2), b)
    with py5.push_matrix():
        py5.rect_mode(py5.CENTER)
        py5.translate(*pos)
        py5.rotate(rot)
        py5.rect(0, 0, w, h)
        py5.rect(0, 0, h, w * (255 - b) / 255)
    
    
def key_pressed():
    if py5.key == 'h':
        out.save(f'out-x{scale_factor}.png')
    else:
        py5.save('out-800.png')
    
py5.run_sketch(block=False)

