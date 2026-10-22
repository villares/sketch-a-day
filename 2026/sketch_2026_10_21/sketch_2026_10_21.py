from itertools import product

import py5
import numpy as np

W = 50

def setup():
    global grid
    py5.size(600, 600)
    py5.color_mode(py5.CMAP, 'viridis', 500)
    grid = list(product(range(50, 551, 100), repeat=2))
    py5.stroke_weight(4)
    make_pairs()
    
def make_pairs():
    global pairs
    rg = py5.random_permutation(grid)
    half = len(rg) // 2
    avs, bvs = rg[:half], rg[half:]
    pairs = [(xa, ya, xb, yb) for (xa, ya), (xb, yb) in zip(avs, bvs)]
 
 
def draw():
    py5.no_loop()
    py5.background('k')
    for l in pairs:
        d = py5.dist(*l)
        py5.stroke(d)
        py5.line(*l)
    py5.stroke('w')
    py5.points(grid)

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        py5.redraw()
    elif py5.key == 'n':
        make_pairs()

py5.run_sketch(block=False)

