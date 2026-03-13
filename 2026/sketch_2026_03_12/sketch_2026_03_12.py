from itertools import combinations, product, chain
from py5_tools import animated_gif


W = 30
M = 5
grid = list(product((-W/2, 0, W/2), repeat=2))
pairs = list(combinations(grid, 2))
combos = list(combinations(pairs, 4))
unconnected_combos = [ 
    combo for combo in combos
    if len(set(chain(*combo))) == 8
]
print(len(combos), len(unconnected_combos))

def setup():
    size((W + M) * 45 + M * 2, (W + M) * 21 + M * 2)
    color_mode(HSB)
    stroke_weight(3)
    #animated_gif('out.gif', duration=0.5, frame_numbers=range(1, 100))
    
#def draw():
    background(0)
    x = 0
    y = 0
    for combo in unconnected_combos:   
        with push_matrix():
            translate(M + x + W / 2, M + y + W / 2)
            for i, (a, b) in enumerate(combo):
                stroke(32 + i * 64, 255, 255)
                line(*a, *b)
        x += W + M
        if x > width - W:
            x = 0
            y += W + M
       
    save('out.png')
