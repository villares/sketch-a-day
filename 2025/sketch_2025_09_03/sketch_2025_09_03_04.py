from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon

def setup():
    global combos, tris, good_pairs, nonoverlapping
    global grid
    py5.size(600, 150)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [Polygon(t) for t in combinations(grid, 3) if Polygon(t).area]

    combos = {Combo((tri,)) for tri in tris}
    combos = sorted(combos, key=lambda c:c.area) 
    print(len(combos)) 
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 10 # columns
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
            
  
class Combo:
    
    def __init__(self, combo):
        self._combo = combo
        self.area = sum(map(lambda p:p.area, combo))
        self.coords = frozenset(self.tri_coords(tri) for tri in combo)
        
    def __len__(self):
        return len(self._combo)
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        
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
            py5.points(grid)
            for poly in self._combo:
                py5.fill(poly.area * 100, 250, 200)
                py5.shape(py5.convert_cached_shape(poly))

    @staticmethod
    def tri_coords(tri):
        return frozenset((x, y) for x, y in tri.exterior.coords[:3])

    @staticmethod
    def rot_coords(coords):
        return frozenset(frozenset((-y, x) for x, y in c)
                         for c in coords)


def key_pressed():
    py5.save('out2.png')

py5.run_sketch(block=False)

