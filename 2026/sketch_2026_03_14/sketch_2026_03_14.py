from itertools import combinations, product, chain
from py5_tools import animated_gif


W = 25
M = 5
grid = list(product((-W/2, 0, W/2), repeat=2))
pairs = list(combinations(grid, 2))
combos = list(combinations(pairs, 3))
unconnected_combos = [ 
    combo for combo in combos
    if len(set(chain(*combo))) == 6 
]
print(len(combos), len(unconnected_combos))

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
