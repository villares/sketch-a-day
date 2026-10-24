from itertools import product

import py5
import numpy as np
import shapely

W = 50

def setup():
    global grid
    py5.size(600, 600)
    py5.color_mode(py5.CMAP, 'plasma', 500)
    grid = list(product(range(50, 551, 100), repeat=2))
    py5.stroke_weight(4)
    make_pairs()
    
def make_pairs():
    global pairs
    rg = py5.random_permutation(grid)
    half = len(rg) // 2
    avs, bvs = rg[:half], rg[half:]
    pairs = [(a, b) for a, b in zip(avs, bvs)]
 
def intersecting(pab, pcd):
    sab = shapely.LineString(pab).buffer(10)
    scd = shapely.LineString(pcd).buffer(10)
    return sab.intersects(scd)
 
def move():
        for i, (a, b) in reversed(list(enumerate(pairs[:-1]))):
            (c, d) = pairs[i + 1]
            if intersecting((a, b), (c, d)):
                if py5.random(100) > 50:
                    a, b = b, a
#                 if py5.random(100) > 50:
#                     c, d = d, c
                pairs[i] = (a, c) 
                pairs[i + 1] = (b, d)
                #sbreak
  
def draw():
    py5.background('k')
    for a, b in pairs:
        d = py5.dist(*a, *b)
        py5.stroke(d)
        py5.line(*a, *b)
    py5.stroke('w')
    py5.points(grid)
    move()

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == 'n':
#         py5.redraw()
        make_pairs()

py5.run_sketch(block=False)

