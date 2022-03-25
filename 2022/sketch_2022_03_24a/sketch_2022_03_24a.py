import py5
from itertools import product, combinations
from math import dist as euclidian_dist # I know py5 has dist() but I want this

def setup():
    global glyphs
    py5.size(800, 800)
    grid_points = list(product(range(-1, 2), repeat=2))
    pairs = combinations(grid_points, 2)
    short_pairs = [(a, b) for a, b in pairs if euclidian_dist(a, b) < 2]
    glyphs = list(combinations(short_pairs, 5))
    print(len(glyphs))
    py5.stroke_weight(3)

def draw():
    py5.background(240)
    s = 10
    x = y = 30 - py5.frame_count  * 30
    for glyph in glyphs:
        for (xa, ya), (xb, yb) in glyph:
            py5.line(x + xa * s, y + ya * s, x + xb * s, y + yb * s)
        x += 30
        if x > py5.width:
            x = 30
            y += 30
        if y > py5.height:
            break
            
py5.run_sketch()
