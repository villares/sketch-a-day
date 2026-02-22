from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon, unary_union, affinity

W = 10
nod = {} # non-overlapping dict
grid = tuple(product((-0.5, 0, 0.5), repeat=2))

def setup():
    global all_tris
    py5.size(900, 1010)
    py5.color_mode(py5.CMAP, 'viridis')
    py5.stroke_join(py5.ROUND)
    #py5.stroke('white')
    py5.no_stroke()
    all_tris = [Polygon(t) for t in combinations(grid, 3)
            if Polygon(t).area]
    start() 
    Polygon.draw = p_draw
    
def start(ns=[3]):
    data_path = Path('shps.data')
#     if not data_path.exists():
#
#     else:
#         combos.update(py5.load_pickle(data_path))
#     print(len(combos))
    for tri in all_tris:
        good = []
        for other in all_tris:
            if other != tri and not other.overlaps(tri):
                good.append(other)
        nod[tri] = good    
    
def draw():
    py5.background('black')
    y = 10
    for k, v in nod.items():
        x = 10
        k.draw(x + W / 2, y + W / 2)
        x += W + 5
        for t in v:
            x += W + 5
            t.draw(x + W / 2, y + W / 2)
        y += W + 3
        if y + W / 2 > py5.height:
            break

# class Combo:
#     
#     def __init__(self, shapes):
#         self.shapes = tuple(shapes)
#         self.vs = frozenset(
#             frozenset((x, y) for x, y in s.exterior.coords)
#             for s in shapes
#         )
#         
#     def draw(self, x, y, s=W):
#         with py5.push_matrix():
#             py5.translate(x, y)
#             py5.scale(s)
#             py5.stroke_weight(1 / s)
#             for i, t in enumerate(self.shapes):
#                 py5.fill(t.area * 2)
#                 py5.shape(t)
#             py5.fill(255)
#             
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#     
#     def __hash__(self):
#         vs = self.vs
#         h = hash(vs)
#         for i in range(3):
#             vs = rot90(vs)
#             h = min(h, hash(vs))
#         return h
#   
# def rot90(combo):
#     return frozenset(frozenset((y, -x) for x, y in pts) for pts in combo)
#     
  
def key_pressed():
    if py5.key == 'r':
        start()
    elif py5.key == 'p':
        py5.save_frame('###.png')
    

def p_draw(self, x, y, s=W):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.scale(s)
        py5.stroke_weight(1 / s)
        py5.fill(self.area * 2)
        py5.shape(self)
  
py5.run_sketch(block=False)


