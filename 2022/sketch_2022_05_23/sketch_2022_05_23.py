# Based on Ahmad Moussa's article https://gorillasun.de/blog/an-algorithm-for-irregular-grids#bool
# via Chris Barber https://twitter.com/code_rgb/status/1528042828219179008
# Code with py5.ixora.io

import py5
from collections import namedtuple
from random import choice, sample, seed

Rect = namedtuple("Rect", "x y w h")

def setup():
    global n_cols, n_rows, col_w, row_h, pad
    py5.size(800, 600)
    seed(0)
    # size of the padding between grid and sketch borders
    pad = py5.width / 12
    # number of rows and columns of the grid
    n_cols = 32
    n_rows = 24
    # actual spacing between grid points
    col_w = (py5.width - pad * 2) / n_cols
    row_h = (py5.height - pad * 2) / n_rows
    generate_grid()
    
def generate_grid():
    global empty_spots, rects
    # here we populate the 2d boolean array
    rects = []
    empty_spots = [[True for _ in range(n_rows)] # collumn
                         for _ in range(n_cols)]
    add_to_grid([4, 1], 2)
    add_to_grid([3, 1], 2)
    for _ in range(5):
        add_to_grid([2, 1])
    add_to_grid([1, 1])

    
def draw():
    py5.background(0)
    py5.stroke_weight(4)
    py5.no_fill()
    for r in rects:
        py5.fill(r.w * 64, 64, r.h * 64)
        py5.rect(r.x * col_w + pad,
                 r.y * row_h + pad,
                 r.w * col_w, r.h * row_h)
    mark_empty()

def add_to_grid(possible_dims, skip=1):
    for x in range(0, n_cols - min(possible_dims) + 1, skip):
        for y in range(0, n_rows - min(possible_dims) + 1, skip):
            # using sample instead of choice to avoid squares, you can use
            # choice twice...
            w, h = sample(possible_dims, 2)
            fits = True
            # check if within bounds
            if x + w > n_cols or y + h > n_rows:
                continue
            # check if rectangle overlaps with any other rectangle
            if fits:
                for xc in range(x, x + w):
                    for yc in range(y, y + h):
                        if empty_spots[xc][yc] == 0:
                            fits = False
                            break
            if fits:
                # mark area as occupied
                for xc in range(x, x + w):
                    for yc in range(y, y + h):
                        empty_spots[xc][yc] = False
                rects.append(Rect(x, y, w, h))

def mark_empty():
    for x in range(n_cols):
        for y in range(n_rows):
            if empty_spots[x][y]:
                py5.point(x * col_w + col_w/2 + pad,
                          y * row_h + row_h/2 + pad)

def key_pressed():
    if py5.key == ' ':
        generate_grid()

py5.run_sketch()
