"""
Combinations of 2 line_segs on octagon, so that the line_segs don't share
starting or ending points: 378
"""
from itertools import combinations

W = 30 # Width base-value for configs
EL_COLOR = 0
GRID_COLOR = 255
SCALE = 2

def setup():
    size(1020 * SCALE, 880 * SCALE, P2D)
    scale(SCALE)
    stroke_cap(ROUND)
    no_fill()
    d45, r = radians(45), 1.5
    positions = [(r * cos(i * d45), r * sin(i * d45)) for i in range(8)]
    pairs_of_points = combinations(positions, 2)        
    line_combos = combinations(pairs_of_points, 2)  # line pairs, no matter order 
    configs = [(a, b) for a, b in line_combos       # pick line_segs that...
               if set(a) != set(b)]     # ...don't have both ends in common

    print(f'Configurations: {len(configs)}')
    i = 1
    x = y = W * 2
    w = W / 3
    for line_segs in configs:
        stroke(GRID_COLOR)
        stroke_weight(w / 3)
        push_matrix()
        translate(x, y)
        points([(xo * w, yo * w) for xo, yo in positions])
        stroke_weight(w / 6)
        stroke(EL_COLOR)
        for (xa, ya), (xb, yb) in line_segs:
            line(xa * w, ya * w,
                      xb * w, yb * w)
        pop_matrix()
        x += W * 1.5
        if x > width / SCALE - W * 1.5:
            #print(i)  # debug
            x = W * 2
            y +=  W * 1.5
        i += 1
    save_frame('sketch_2022_11_07.png')
