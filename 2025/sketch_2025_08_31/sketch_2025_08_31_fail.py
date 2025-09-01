from itertools import product, permutations, combinations
from itertools import combinations_with_replacement
from pathlib import Path
from functools import cache

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString
from shapely import unary_union

@cache
def CachedPolygon(*args):
    return Polygon(*args)

def setup():
    global combos, tris
    py5.size(24 * 40, 24 * 40)
    py5.color_mode(py5.HSB)
    #animated_gif('out.gif', duration=1.2, frame_numbers=range(1, 13+1))
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [t for t in combinations(grid, 3) if CachedPolygon(t).area]
    allcombos = []
    a4allcombos = []
    for n in range(2, 6 + 1):
        if Path(f'a4ncombos{n}.data').is_file():
            m = py5.millis()
            a4ncombos = py5.load_pickle(f'a4ncombos{n}.data')
            a4allcombos.extend(a4ncombos)
            print(f'time to load {n}combos pickle {py5.millis()-m}')
        else: 
            m = py5.millis()
            ncombos = [
                tuple(map(CachedPolygon, combo))
                for combo in combinations(tris, n)]
            allcombos.extend(ncombos)
            print(n, len(ncombos))
            py5.save_pickle(ncombos, f'ncombos{n}.data')
            a4ncombos = [
                combo for combo in ncombos
                if sum(map(lambda p:p.area, combo)) == 4
            ]
            py5.save_pickle(a4ncombos, f'a4ncombos{n}.data')
            a4allcombos.extend(a4ncombos)
            print(f'time to calculate {n}combos {py5.millis()-m}')
            
#     m = py5.millis()
#     square_combos = [
#         combo for combo in a4allcombos
#         if unary_union(combo).area == 4
#     ]
#     print(f'time to pick only square combos {py5.millis()-m}')
    combos = a4allcombos  # combos to draw
    print(len(a4allcombos)) #, len(square_combos))
    # pick only the full square ones
    
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 24 # rows and columns
    i = 0 # py5.frame_count * N * N
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
            py5.stroke_weight(1 / w)
            combo = combos[ci]
            for poly in combo:
                py5.fill(poly.area * 100, 200, 200)
                py5.shape(py5.convert_cached_shape(poly))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

