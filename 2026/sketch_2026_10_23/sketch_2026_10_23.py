from itertools import product

import py5
import numpy as np
import shapely

W = 50

def setup():
    global grid
    py5.size(600, 600)
    py5.color_mode(py5.CMAP, 'cividis_r', 500)
    grid = list(product(range(50, 551, 100), repeat=2))
    make_pairs()
    
def make_pairs():
    global pairs, pairs_idx
    rg = py5.random_permutation(grid)
    half = len(rg) // 2
    avs, bvs = rg[:half], rg[half:]
    pairs = [(a, b) for a, b in zip(avs, bvs)]
    pairs_idx = list(range(len(pairs)))

def move():
    # this is a problem! not like random.sample() the default is dereplace=True
    i, j = py5.random_sample(pairs_idx, 2)   
    a, b = pairs[i]
    c, d = pairs[j]
    od = py5.dist(*a, *b) + py5.dist(*c, *d)
    nd = py5.dist(*a, *c) + py5.dist(*b, *d)
    if nd < od:
        pairs[i] = a, c
        pairs[j] = b, d
        #print(len(pairs)) 
  
def draw():
    py5.background('k')
    py5.stroke_weight(3)
    for a, b in pairs:
        d = py5.dist(*a, *b)
        py5.stroke(d)
        py5.line(*a, *b)
    py5.stroke_weight(5)    
    py5.stroke('w')
    py5.points(grid)
    py5.stroke('r')

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == 'n':
        make_pairs()
    elif py5.key == 'm':
        move()
        

py5.run_sketch(block=False)

