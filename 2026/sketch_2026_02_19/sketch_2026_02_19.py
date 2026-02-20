# 244 triangle subivisions

from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon, unary_union

W = 39
tris = []
grid = tuple(product((-1, 0, 1), repeat=2))

def setup():
    global all_tris
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    all_tris = [Polygon(t) for t in combinations(grid, 3)
            if Polygon(t).area]
    start() 
    
def start(ns=[6]):
    data_path = Path('tris6.data')
    tris.clear()
    if not data_path.exists():
        for n in ns:
            tris.extend(
                c for c in combinations(all_tris, n)
                if sum(t.area for t in c) == 4 and unary_union(c).area == 4
            )
        py5.save_pickle(tris, data_path)
    else:
        tris[:] = py5.load_pickle(data_path)
    print(len(tris))
    
    
def draw():
    py5.background(0)
    x = 10
    y = 10
    for tri in tris:
        draw_combo(tri, x + W / 2, y + W / 2)
        x += W + 10
        if x + W / 2 > py5.width:
            x = 10
            y += W + 10
        if y + W / 2 > py5.height:
            break

def draw_combo(combo, x, y, s=W):
    with py5.push_matrix():
        py5.translate(x, y)
        w = s / 2 
        py5.scale(w)
        py5.stroke_weight(1 / w)
        for i, t in enumerate(combo):
            py5.fill(64 + t.area * 96, 255, 255)
            py5.shape(t)
    
  
def key_pressed():
    if py5.key == 'r':
        start()
    elif py5.key == 'p':
        py5.save_frame('###.png')
    
        
py5.run_sketch(block=False)