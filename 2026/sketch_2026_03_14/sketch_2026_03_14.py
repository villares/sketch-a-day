# This is a py5 "imported mode" sketch, you'll need a "sketch runner"
# learn about py5 modes at https://py5coding.org

from itertools import combinations, product, chain

W = 25   # combo width
M = 5    # spacing
grid = list(product((-W/2, 0, W/2), repeat=2))  # the 3x3 grid
pairs = list(combinations(grid, 2))     # all possible segments
combos = list(combinations(pairs, 3))   # all 3 segment combinations
unconnected_combos = [ 
    combo for combo in combos
    if len(set(chain(*combo))) == 6    # 6 distinct vertices
]
print(len(combos), len(unconnected_combos)) # 7140 1260

def setup():
    size((W + M) * 60 + M * 2, (W + M) * 21 + M * 2)
    color_mode(CMAP, 'tab20b', 360)
    stroke_weight(3)
    background('black')    
    x = 0
    y = 0
    for combo in sorted(unconnected_combos):   
        with push_matrix():
            translate(M + x + W / 2, M + y + W / 2)
            for i, ((xa, ya), (xb, yb)) in enumerate(combo):
                ang = (atan2(ya - yb, xa - xb) + PI) % PI
                #stroke(degrees(ang * 2))
                stroke(dist(xa, ya, xb, yb) * 10)
                line(xa, ya, xb, yb)
        x += W + M
        if x > width - W:
            x = 0
            y += W + M
       
    save('out.png')
