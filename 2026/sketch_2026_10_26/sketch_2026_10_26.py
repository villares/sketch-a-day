# broken

from itertools import product

import py5
import numpy as np
import shapely

M = 100
t = 0

def setup():
    global grid, buffer
    py5.size(800, 600)
    py5.color_mode(py5.CMAP, 'spring', 500)
    font = py5.create_font('Tomorrow Bold', 700)
    buffer = py5.create_graphics(py5.width, py5.height)
    buffer.begin_draw()
    buffer.fill(255)
    buffer.text_font(font)
    buffer.text_align(py5.CENTER, py5.CENTER)
    buffer.text("26", py5.width / 2, py5.height / 2)
    buffer.end_draw()
    grid = [(x, y) for x, y in product(
        range(M // 2, py5.width + 1 - M // 2, M),
        range(M // 2, py5.height + 1 - M // 2, M)
        ) #if buffer.get_pixels(x, y) == py5.color('w')
    ]
    make_pairs()
    py5.random_seed(0)
    
    
def make_pairs():
    global pairs, pairs_idx, next_pairs
    rg = py5.random_permutation(grid)
    half = len(rg) // 2
    avs, bvs = rg[:half], rg[half:]
    pairs = np.array([(a, b) for a, b in zip(avs, bvs)])
    next_pairs = pairs.copy()

def seg_len(seg):
    a, b = seg
    return py5.dist(*a, *b)

def move():
    #pairs.sort(key=seg_len, reverse=True)
    pairs_idx = range(len(pairs))
    next_pairs = pairs.copy()
    if py5.frame_count % 2 == 0:
        i = 0
        j = py5.random_choice(range(1, len(pairs)))
    else:
        i, j = py5.random_sample(pairs_idx, 2, replace=False)
    a, b = pairs[i]
    c, d = pairs[j]
    od = py5.dist(*a, *b) + py5.dist(*c, *d)
    nd = py5.dist(*a, *c) + py5.dist(*b, *d)
    if nd < od:
        next_pairs[i] = a, c
        next_pairs[j] = b, d
        #py5.save_frame('out/###.png')
    else:
        pairs[i] = b, a
        

  
def draw():
    global t
    py5.background('k')
    #py5.image(buffer, 0, 0)
    py5.stroke_weight(5)
    t = py5.mouse_x / py5.width
    l_pairs = py5.lerp(pairs, next_pairs, t)
    for a, b in l_pairs:
        d = py5.dist(*a, *b)
        py5.stroke(d)
        py5.line(*a, *b)
    py5.stroke_weight(5)    
    py5.stroke('w')
    py5.points(grid)
    #if t == 1:
    move()
    #sss    t = 0


def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == 'n':
        make_pairs()
    elif py5.key == 'm':
        move()
        print(len(pairs))
        
py5.run_sketch(block=False)


