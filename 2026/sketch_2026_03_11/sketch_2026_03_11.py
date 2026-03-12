from itertools import combinations, product, chain
from py5_tools import animated_gif

grid = list(product((-50, 0, 50), repeat=2))
pairs = list(combinations(grid, 2))
combos = list(combinations(pairs, 4))

continuos = [ 
    combo for combo in combos
    if len(set(chain(*combo))) <= 4
]
print(len(combos), len(continuos))

def setup():
    size(600, 600)
    color_mode(HSB)
    frame_rate(10)
    animated_gif('out.gif', duration=0.5, frame_numbers=range(1, 100))
    
def draw():
    background(0)
    translate(300, 300)
    scale(5)
    combo = continuos[frame_count % len(continuos)]
    for i, (a, b) in enumerate(combo):
        translate(0.1, 0.5)
        stroke(i * 64, 255, 255, 150)
        line(*a, *b)


