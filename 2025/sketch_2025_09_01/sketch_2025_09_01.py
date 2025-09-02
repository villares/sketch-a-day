from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon


def setup():
    global combos, tris
    py5.size(19 * 50, 4 * 50)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [Polygon(t) for t in combinations(grid, 3) if Polygon(t).area]
    combos = [(tri,) for tri in tris]
    print(len(combos))
    
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 19 # rows and columns
    i = 0 # py5.frame_count * N * N
    s = py5.width / N
    w = s / 2 - 5
    for r in range(N):
        for c in range(N):
            x = s / 2 + s * c
            y = s / 2 + s * r
            draw_combo(i, x, y, w)
            i += 1
            
def draw_combo(ci, x, y, w):
    if ci < len(combos):
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(w)
            py5.stroke_weight(1 / w)
            combo = combos[ci]
            for poly in combo:
                py5.fill(poly.area * 100, 200, 200)
                py5.shape(py5.convert_cached_shape(poly))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

