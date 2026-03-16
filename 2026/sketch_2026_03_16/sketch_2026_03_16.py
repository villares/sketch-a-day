# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

from itertools import combinations, product, chain

import py5
from shapely import Polygon
import numpy as np

W = 30   # combo width
M = 20    # spacing
COLS = 19
ROWS = 12

def setup():
    py5.size((W + M) * COLS + M, (W + M) * ROWS + M)
    py5.color_mode(py5.CMAP, 'tab20b', py5.dist(W, W, 0, 0))
    py5.stroke_weight(4)
    generate_combos()
    
def draw():
    py5.background('black')    
    x = 0
    y = 0
    for combo in sorted(combos, key=sum_seg_len):   
        with py5.push_matrix():
            py5.translate(M + x + W / 2, M + y + W / 2)
            for i, ((xa, ya), (xb, yb)) in enumerate(combo):
                py5.stroke(py5.dist(xa, ya, xb, yb))
                py5.line(xa, ya, xb, yb)
        x += W + M
        if x > py5.width - W - M:
            x = 0
            y += W + M
       
def key_pressed():
    py5.save_frame('###.png')

def generate_combos():
    global combos
    grid = list(product((-W/2, 0, W/2), repeat=2))  # the 3x3 grid
    pairs = list(combinations(grid, 2))        # all possible segments
    all_combos = list(combinations(pairs, 2))  # all 2-segment combos
    combos = [ 
        combo for combo in all_combos
        if good_combo(combo)  # connected but not aligned
    ]
    print(len(all_combos), len(combos)) # 630 228

def good_combo(combo):
    for a, b in combinations(combo, 2):
        if not valid_segments(a, b):
            return False
    return True

def valid_segments(a, b):
    unique_vs = set(a) | set(b)
    if len(unique_vs) == 4:
        return False
    return Polygon(unique_vs).area != 0

def sum_seg_len(combo):
    return sum(
        py5.dist(xa, ya, xb, yb) 
        for (xa, ya), (xb, yb) in combo
    )


py5.run_sketch(block=False)