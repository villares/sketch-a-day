
from itertools import product, combinations, permutations
from pathlib import Path

import py5
from shapely import Polygon, LineString


def setup():
    global combos
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [Polygon(t) for t in combinations(grid, 3) if Polygon(t).area]
    combos = [Combo([tri]) for tri in tris]
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
    
    def __init__(self, combo=None):
        if combo is None:
            combo = [Polygon()]
        self._combo = combo
        self.area = sum(map(lambda p:p.area, combo))
        self.coords = frozenset(self.tri_coords(tri) for tri in combo)
        self.ls = LineString(((-1, -1), (0, -1)))     
        self.over = False
        for t in combo:
            if t.touches(self.ls):
                self.over = True
        
        
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
            py5.stroke(255, self.over * 255, 0)
            py5.shape(self.ls)
            
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

