from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon

def setup():
    global combos, tris, good_pairs, nonoverlapping
    global grid
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [Polygon(t) for t in combinations(grid, 3) if Polygon(t).area]
#     # get all the 23903 nonoverlapping combinations of triangles
#     # some will fill the grid, others will have gaps, I'll filter later
#     if Path(f'nonoverlapping.data').is_file():
#         nonoverlapping = py5.load_pickle(f'nonoverlapping.data')
#     else:
#         m = py5.millis()
#         nonoverlapping_pairs = [(a, b) for a, b in combinations(tris, 2)
#           if not (a.overlaps(b)
#           or a.contains(b)
#           or b.contains(a))
#           ]
#         good_pairs = set(nonoverlapping_pairs)
#         good_pairs.update((b, a) for a, b in nonoverlapping_pairs)
#         nonoverlapping = set(nonoverlapping_pairs)
#         starter = nonoverlapping_pairs
#         for i in range(6):
#             new_combos = []
#             for combo in starter:
#                 for tri in tris:
#                     for item in combo:
#                         if (tri, item) not in good_pairs:
#                             break
#                     else:
#                         new_combo = combo + (tri,)
#                         nonoverlapping.add(frozenset(new_combo))            
#                         new_combos.append(new_combo)
#             starter = new_combos
#         py5.save_pickle(nonoverlapping, f'nonoverlapping.data')
#         print(f'{len(nonoverlapping)} nonoverlapping combos {py5.millis()-m}')
#     # Filter out combinations that do not fill the entire grid
#     # And remove rotations!
#     combos = {Combo(combo) for combo in nonoverlapping
#               if sum(map(lambda p:p.area, combo)) == 4}
    combos = {Combo((tri,)) for tri in tris}
    combos = sorted(combos, key=lambda c:c.area) 
    print(len(combos)) 
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 9 # columns
    i = 0 # py5.frame_count * N * N
    s = py5.width / N
    w = s / 2 - 15
    for r in range(N):
        for c in range(N):
            x = s / 2 + s * c
            y = s / 2 + s * r
            if i < len(combos):
                combos[i].draw(x, y, w)
            i += 1
            

def tri_coords(tri):
    return tuple(sorted((x * 0.9, y * 0.9) for x, y in tri.exterior.coords[:3]))

def rot90(coords):
    return tuple((-y, x) for x, y in coords)

def get_combo_coords(combo):
    return tuple(sorted(tri_coords(tri) for tri in combo))

def rot_combo_coords(coords):
    return tuple(sorted(rot90(c) for c in coords))
    
class Combo:
    
    def __init__(self, combo):
        self._combo = combo
        self.area =sum(map(lambda p:p.area, combo))
        
    def __len__(self):
        return len(self._combo)
    
    def __eq__(self, other):
        return hash(self) == hash(other)
#         
    def __hash__(self):
        c = get_combo_coords(self._combo)
        h = hash(c)
        for _ in range(3):
            c = rot_combo_coords(c)
            rh = hash(c)
            h = min(h, rh)
        return h
    

    def draw(self, x, y, w):
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(w)
            py5.stroke_weight(2 / w)
            py5.stroke(255)
            py5.points(grid)
            for poly in self._combo:
                py5.fill(poly.area * 100, 250, 200)
                py5.shape(py5.convert_cached_shape(poly))
            

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

