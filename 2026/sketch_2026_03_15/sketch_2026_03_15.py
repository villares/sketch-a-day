# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

from itertools import combinations, product, chain

import py5

W = 30   # combo width
M = 20    # spacing
COLS = 21
ROWS = 18
grid = list(product((-W/2, 0, W/2), repeat=2))  # the 3x3 grid
pairs = list(combinations(grid, 2))     # all possible segments
combos = list(combinations(pairs, 2))   # all 2 segment combinations
unconnected_combos = [ 
    combo for combo in combos
    if len(set(chain(*combo))) == 4    # 4 distinct vertices
]
print(len(combos), len(unconnected_combos)) # 630 378

def setup():
    py5.size((W + M) * COLS + M, (W + M) * ROWS + M)
    py5.color_mode(py5.CMAP, 'tab20b', py5.dist(W, W, 0, 0))
    py5.stroke_weight(4)
    py5.background('black')    
    x = 0
    y = 0
    for combo in sorted(unconnected_combos, key=sum_seg_len):   
        with py5.push_matrix():
            py5.translate(M + x + W / 2, M + y + W / 2)
            for i, ((xa, ya), (xb, yb)) in enumerate(combo):
                #ang = (atan2(ya - yb, xa - xb) + PI) % PI
                #stroke(degrees(ang * 2))
                py5.stroke(py5.dist(xa, ya, xb, yb))
                py5.line(xa, ya, xb, yb)
        x += W + M
        if x > py5.width - W - M:
            x = 0
            y += W + M
       
    py5.save('out.png')

def sum_seg_len(combo):
    return sum(
        py5.dist(xa, ya, xb, yb) 
        for (xa, ya), (xb, yb) in combo
    )
py5.run_sketch(block=False)