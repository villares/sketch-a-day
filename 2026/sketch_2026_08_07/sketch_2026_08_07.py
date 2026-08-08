# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

from itertools import product

import py5
from py5_tools import animated_gif
import numpy as np


N = 5   # 25 elements (5 x 5 grid)
elements = []

def setup():
    global grid
    py5.size(600, 600, py5.P2D)
    py5.rect_mode(py5.CENTER)
    grid = list(product(range(N), range(N)))
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_font(py5.create_font('Tomorrow', 30))
    #py5.text_size(W/2)
    py5.fill(0)
    animated_gif('out.gif',
                 frame_numbers=range(1, 231, 2),
                 duration=0.05)

def phase():
    f = py5.frame_count
    if f <= 101:
        amt = (f - 1) / 100
        return 1, amt
    elif f <= 131:
        return 1, 1
    elif f <= 231:
        amt = (f - 131) / 100
        return 2, amt
    else:
        return 2, 1
    
def draw(): 
    py5.background(200)
    py5.no_fill()
    p, amt = phase()

    if p == 1:
        W = py5.remap(amt, 0, 1, 50, 100)
        xy_grid = np.array([(W + i * W, W + j * W) for i, j in grid])
        xy_col = np.array([(py5.width / 2, W + k * W)
                           for k, _ in enumerate(grid)])    
        xy_pos = py5.lerp(xy_col, xy_grid, amt)
        py5.text_size(W/3)
        for (x, y), (i,j) in zip(xy_pos, grid):
            py5.square(x, y, W)
            py5.text(f'{i}, {j}', x, y)
    else:
        W = py5.remap(amt, 0, 1, 100, 50)
        xy_grid = np.array([(W + i * W, W + j * W) for i, j in grid])
        xy_row = np.array([(W + k * W, py5.height / 2)
                           for k, _ in enumerate(grid)])    
        xy_pos = py5.lerp(xy_grid, xy_row, amt)
        py5.text_size(W/3)
        for (x, y), (i,j) in zip(xy_pos, grid):
            py5.square(x, y, W)
            py5.text(f'{i}, {j}', x, y)


def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')

py5.run_sketch(block=False)
