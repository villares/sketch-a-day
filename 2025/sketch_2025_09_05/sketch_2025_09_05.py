# revisiting sketch_2025_08_27 to remove rotations

from itertools import product, permutations
from pathlib import Path

import py5
from shapely import Polygon

data_file = 'polys.data'

def setup():
    global combos, tris, good_pairs, nonoverlapping
    py5.size(1700, 300)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    if Path(data_file).is_file():
        combos = py5.load_pickle(data_file)
    else:
        combos = set() 
        for a, b, c, d, e, f, g, h, i in permutations(grid, 9):
           t0 = Polygon((a, b, c))
           t1 = Polygon((d, e, f))
           t2 = Polygon((g, h, i))
           if t0.area and t1.area and t2.area:
               combos.add(Combo((t0, t1, t2)))
        combos = sorted(combos)
        py5.save_pickle(combos, data_file)
    print(len(combos)) 
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 17 # columns
    i = 0 # py5.frame_count * N * N
    s = py5.width / N
    w = s / 2 - 15
    for r in range(N - 1):
        for c in range(N):
            x = s / 2 + s * c
            y = s / 2 + s * r
            if i < len(combos):
                combos[i].draw(x, y, w)
            i += 1
            
    
class Combo:
    
    def __init__(self, combo):
        self._combo = combo
        self.area = sum(map(lambda p:p.area, combo))
        self.coords = frozenset(self.tri_coords(tri) for tri in combo)
        
    def __len__(self):
        return len(self._combo)
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __lt__(self, other):
        return self.area < other.area
        
    def __hash__(self):
        c = self.coords
        h = hash(c)
        for _ in range(3):
            c = self.rot_coords(c)
            rh = hash(c)
            h = min(h, rh)
        return h
    
    def draw(self, x, y, w):
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(w)
            py5.stroke_weight(2 / w)
            py5.stroke(255)
            for poly in self._combo:
                py5.fill(255, 64)
                py5.shape(py5.convert_cached_shape(poly))

    @staticmethod
    def tri_coords(tri):
        return frozenset((x, y) for x, y in tri.exterior.coords[:3])

    @staticmethod
    def rot_coords(coords):
        return frozenset(frozenset((-y, x) for x, y in c)
                         for c in coords)

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

