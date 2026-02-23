from itertools import product, combinations

import py5
from shapely import Polygon, unary_union, affinity

W = 50
M = 10
nod = {} # non-overlapping dict
grid = tuple(product((-0.5, 0, 0.5), repeat=2))
seeds = set()
s_combos = []

def setup():
    global all_tris
    py5.size((W + M) * 18 + M, (W + M) * 15 + M)
    py5.color_mode(py5.CMAP, 'viridis')
    py5.stroke_join(py5.ROUND)
    py5.stroke('black')
    all_tris = [Polygon(t) for t in combinations(grid, 3)
            if Polygon(t).area]    
    # prepare the dict of non-overlapping triangles
    for tri in all_tris:
        good = []
        for other in all_tris:
            if other != tri and (tri.union(other)).area == tri.area + other.area:                good.append(other)
        nod[tri] = good
        
    for tri in all_tris:
        others = nod[tri]
        for other in others:
            seeds.add(Combo([tri, other]))
    print(len(seeds))
    s_combos[:] = sorted(
        seeds,
        key=lambda c: c.areas
    )            

#def draw():
    py5.background('black')
    y = M
    x = M
    i = 0
    for c in s_combos:
        c.draw(x + W / 2, y + W / 2)
        i += 1
        x += W + M
        if x + W > py5.width:
            x = M
            y += W + M
        if y + W > py5.height:
            break
    print('shown', i)
        
class Combo:
    
    def __init__(self, shapes):
        self.shapes = tuple(shapes)
        self.fsovs = frozenset(  # frozenset of frozensets of vertives
            frozenset((x, y) for x, y in s.exterior.coords)
            for s in shapes
        )
        self.areas = sorted(s.area for s in shapes)
        
    def draw(self, x, y, s=W):
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(s)
            py5.stroke_weight(1 / s)
            for i, t in enumerate(self.shapes):
                py5.fill(t.area * 2)
                py5.shape(t)
            py5.fill(255)
            
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        vs = self.fsovs
        h = hash(vs)
        for i in range(3):
            vs = rot90(vs)
            h = min(h, hash(vs))
        return h
  
def rot90(fsovs):
    return frozenset(frozenset((y, -x) for x, y in pts) for pts in fsovs)
    
def key_pressed():
    if py5.key == 'p':
        py5.save_frame('###.png')
    
py5.run_sketch(block=False)




