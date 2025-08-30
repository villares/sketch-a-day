from itertools import product, permutations, combinations
from itertools import combinations_with_replacement

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString
from shapely import unary_union

def setup():
    global combos
    py5.size(24 * 40, 24 * 40)
    animated_gif('out.gif', duration=1.2, frame_numbers=range(1, 7+1))
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [t for t in combinations(grid, 3) if Polygon(t).area]
    combos = [(Polygon(a), Polygon(b), Polygon(c))
              for a, b, c in combinations(tris, 3)]
    # filter out overlapping polys
    combos = [(pa, pb, pc) for pa, pb, pc in combos
              if unary_union((pa, pb, pc)).area == pa.area + pb.area + pc.area]
    
    print(len(combos))
            
def draw():
    py5.background(100)
    py5.fill(255, 200)
    N = 24 # rows and columns
    i = py5.frame_count * N * N
    s = 40
    w = 15
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
            combo = combos[ci]
            for poly in combo:
                py5.stroke_weight(1 / w)
                py5.shape(py5.convert_cached_shape(poly))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

