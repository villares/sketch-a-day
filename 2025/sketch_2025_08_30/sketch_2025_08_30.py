from itertools import product, permutations, combinations
from itertools import combinations_with_replacement
from pathlib import Path
from functools import cache
import pickle

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString
from shapely import unary_union

@cache
def CachedPolygon(*args):
    return Polygon(*args)

def setup():
    global combos
    py5.size(24 * 40, 24 * 40)
    py5.color_mode(py5.HSB)
    animated_gif('out.gif', duration=1.2, frame_numbers=range(1, 13+1))
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    if Path('out.data').is_file():
        with open('out.data', 'rb') as f:
            combos = pickle.load(f)
    else:
        tris = [t for t in combinations(grid, 3) if CachedPolygon(t).area]
        combos = [tuple(map(CachedPolygon, combo))
                  for combo in combinations(tris, 4)]
        # filter out overlapping polys
        combos = [(pa, pb, pc, pd) for pa, pb, pc, pd in combos
                  if unary_union((pa, pb, pc, pd)).area
                  == pa.area + pb.area + pc.area + pd.area]
        with open('out.data', 'wb') as f:
            pickle.dump(combos, f)
    
    print(len(combos))
            
def draw():
    py5.background(0)
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
            py5.stroke_weight(1 / w)
            combo = combos[ci]
            for poly in combo:
                py5.fill(poly.area * 100, 200, 200)
                py5.shape(py5.convert_cached_shape(poly))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

