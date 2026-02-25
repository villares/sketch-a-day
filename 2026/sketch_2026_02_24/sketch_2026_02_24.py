from itertools import product, combinations

import py5
from shapely import Polygon, unary_union, simplify

W = 25
M = 4
nod = {} # non-overlapping dict
grid = tuple(product((-0.5, 0, 0.5), repeat=2))
s_combos = []

def setup():
    global all_tris
    py5.size((W + M) * 30 + M, (W + M) * 27 + M)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 25)
    py5.stroke_weight(0.5)
    py5.stroke_join(py5.ROUND)
    py5.stroke('black')
    all_tris = [Polygon(t) for t in combinations(grid, 3)
            if Polygon(t).area]    
    # prepare the dict of non-overlapping triangles
    for tri in all_tris:
        good = set()
        for other in all_tris:
            union_area = tri.union(other).area
            if other != tri and union_area == tri.area + other.area:
                good.add(other)
        nod[tri] = good
    # first pair of triangles as seeds
    seeds = set()
    for tri in all_tris:
        others = nod[tri]
        for other in others:
            seeds.add(Combo([tri, other]))
    #print(len(seeds)) # 270
    # collecting the full squares and growing the combos adding more triangles
    while seeds:
        for s in seeds:
            if s.area == 1:
                s_combos.append(s)
        new_seeds = set()
        for combo in seeds:
            others = set.intersection(*[nod[s] for s in combo.shapes])
            for other in others:
                 new_seeds.add(Combo(combo.shapes + (other,))) 
        seeds = new_seeds
        #print(len(seeds))      
    print(f'{len(s_combos)}')
    # now start the merging of triangles
    seeds.clear()
    seeds.update(s_combos)
    
    for s in seeds.copy():
        seeds.update(merge_pairs(s))    
    s_combos[:] = sorted(seeds, key=lambda c: c.areas)
    
    print(f'{len(s_combos)}')
    
def merge_pairs(combo):
    shapes = set(combo.shapes)
    return [
        Combo(shapes - set(pair) | {simplify(u, 0.01),})
        for pair in combinations(combo.shapes, 2)
        if len(shapes) > 2
        and isinstance(u := unary_union(pair), Polygon) and u.is_simple
    ]

    
def draw():
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
    #print('shown', i)
    
    
class Combo:
    
    def __init__(self, shapes):
        self.shapes = tuple(shapes)
        self.fsovs = frozenset(  # frozenset of frozensets of triangle vertices
            frozenset((x, y) for x, y in tuple(s.exterior.coords)[:-1])
            for s in shapes
        )
        self.areas = sorted((s.area for s in shapes), reverse=True)
        self.area = sum(self.areas)
        
    def draw(self, x, y, s=W):
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(s)
            py5.stroke_weight(1 / s)
            for i, t in enumerate(self.shapes):
                py5.fill(len(t.exterior.coords) * 4)
                py5.shape(t)
            py5.fill(255)
            
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        vs = self.fsovs
        h = hash(vs)
        for i in range(3):
            vs = self.rot90(vs)
            h = min(h, hash(vs))
        return h
    
    @staticmethod  
    def rot90(fsovs):
        return frozenset(frozenset((y, -x) for x, y in pts) for pts in fsovs)
    
def key_pressed():
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == 's':
        process_seeds()
    
py5.run_sketch(block=False)






