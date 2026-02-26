from itertools import product, combinations
import math

import py5
from shapely import Polygon, unary_union, simplify, make_valid
import numpy as np

W = 16
M = 2
nod = {} # non-overlapping dict
grid = tuple(product((-0.5, 0, 0.5), repeat=2))
s_combos = []

def setup():
    global all_tris
    py5.size((W + M) * 89 + M, (W + M) * 11 + M)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.JET, 255)
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
    print(f'{len(s_combos)} triangle configurations')
    # now start the merging of triangles
    seeds.clear()
    seeds.update(s_combos) 
    new_seeds = set()
    base_seeds = seeds.copy()
    for _ in range(5):
        for s in base_seeds:
            new_seeds.update(merge_pairs(s))
        seeds.update(new_seeds)
        base_seeds = new_seeds.copy()
    # order by areas
    s_combos[:] = sorted(seeds, key=lambda c: c.areas)
    print(f'{len(s_combos)} total configurations')
    
def merge_pairs(combo):
    shapes = set(combo.shapes)
    return [
        Combo(shapes - set(pair) | {simplify_by_angle(u).simplify(0.1),})
        for pair in combinations(combo.shapes, 2)
        if len(shapes) > 2
        and isinstance(u := unary_union(pair), Polygon)
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
                vcount = len(t.exterior.coords) - 1
                py5.fill(vcount / 7 * 255)
                py5.shape(t)
            py5.fill(255)
            
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        vs = self.fsovs
        h = hash(vs)
        for i in range(3):  # rotate 90 degrees
            vs = frozenset(frozenset((y, -x) for x, y in pts) for pts in vs)
            h = min(h, hash(vs))
        return h
    
# https://github.com/shapely/shapely/issues/1046#issuecomment-1137778410

def get_angles(vec_1, vec_2):
    dot = np.dot(vec_1, vec_2)
    det = vec_1[...,0] * vec_2[...,1] - vec_1[...,1] * vec_2[...,0]
    angle_in_rad = np.arctan2(det,dot)
    return np.degrees(angle_in_rad)
    
def simplify_by_angle(poly_in, deg_tol=1):
    '''Try to remove persistent coordinate points that remain after
    simplify, convex hull, or something, etc. with some trig instead
    poly_in: shapely Polygon
    deg_tol: degree tolerance for comparison between successive vectors
    '''
    ext_poly_coords = poly_in.exterior.coords[:]
    vector_rep = np.diff(ext_poly_coords, axis=0)
    num_vectors = len(vector_rep)
    angles_list = []
    for i in range(0, num_vectors):
        angles_list.append(np.abs(get_angles(vector_rep[i], vector_rep[(i + 1) % num_vectors])))
    #   get mask satisfying tolerance
    thresh_vals_by_deg = np.where(np.array(angles_list) > deg_tol)
    new_idx = list(thresh_vals_by_deg[0] + 1)
    new_vertices = [ext_poly_coords[idx] for idx in new_idx]
    return Polygon(new_vertices) 
    
    
def key_pressed():
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == 's':
        process_seeds()
    
py5.run_sketch(block=False)





