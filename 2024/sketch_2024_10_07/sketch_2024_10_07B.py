"""
512 ways of making enclosed areas i a square turning on/off positions
in a 3 x 3 grid (9 sub-squares).

9 squares with 2 possible configurations 2 ** 9 -> 512
Clor hue varies with the area and the squares are ordered with
the less filled on top left, and the most filled on the bottom right.
"""

from itertools import product, combinations
from functools import cache

import py5  # check out https://github.com/py5coding 
from shapely import Polygon, MultiPolygon, unary_union

N = 3 # default grid "order", generates N * N square cells
ensembles = []

def setup():
    py5.size(32 * 47 + 100, 16 * 47 + 100)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    m = py5.millis()
    start()
    print(py5.millis() - m)
    
def draw():
    py5.background(0)
    py5.translate(50, 50) # notice the + 100 on size()
    Region.S = 15
    ensemble_margin = 1
    S = Region.S * N + ensemble_margin * 2 # 32
    k = 0
    for j in range(16):
        y = j * S
        for i in range(32):
            x = i * S
            if k < len(ensembles):
                draw_ensemble(
                    ensembles[k],
                    x + ensemble_margin,
                    y + ensemble_margin)
            k += 1
    
def draw_ensemble(ensemble, xe, ye):
    with py5.push_matrix():
        py5.translate(xe, ye)
        for region in ensemble:
            region.draw()
 
def start():
    ensembles.clear()
    SQUARE_TYPES = (# diagonal, filled a, filled b
        (0, 0, 0),  
        (0, 1, 1),  
        (0, 2, 2),
#         (0, 3, 3)
    )
    # This would remove the distintion of colors
    ensembles[:] = sorted({generate_ensemble(squares) for squares
                       in product(SQUARE_TYPES, repeat=N*N)},
                       key=len)
  #  ensembles[:] = sorted((generate_ensemble(squares) for squares
  #                     in product(SQUARE_TYPES, repeat=N*N)),
  #                     key=ensemble_area)
    print(f'Partitions: {len(ensembles)}')
    
def ensemble_area(ensemble):
    """Filled region area"""
    return sum(region.p.area for region in ensemble
               if region.filled)
    
def generate_ensemble(squares):
    regions = set()
    for (i, j), (t, a, b) in zip(product(range(N), repeat=2),
                                   squares):
        if t == 1:
            ra = Region([(i, j), (i + 1, j), (i + 1, j + 1)], a)
            rb = Region([(i, j), (i, j + 1), (i + 1, j + 1)], b)
        else:
            ra = Region([(i, j), (i + 1, j), (i, j + 1)], a)
            rb = Region([(i, j + 1), (i + 1, j), (i + 1, j + 1)], b)           
        regions.update((ra, rb))
    Region.merge_regions(regions)
    return frozenset(regions)
  
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')


class Region:
    
    S = 225 # default grid cell size
    
    
    def __init__(self, p, filled=0):
        self.p = cached_polygon(tuple(p)) if isinstance(p, list) else p
        self.shp = py5.convert_cached_shape(self.p)
        self.shp.disable_style()
        self.filled = filled
        
    def __repr__(self):
        return f'Region({self.p}, filled={self.filled})' 
        
    def __eq__(self, other):
        return self.p.area == other.p.area
    
    def __gt__(self, other):
        return self.p.area > other.p.area
    
    def __hash__(self):
        return hash(self.p) + hash(self.filled)
    
    @cache
    def isadjacent(self, other):
        return self.p.exterior.overlaps(other.p.exterior)
 
    def draw(self, s=None):
        s = s or self.S
        with py5.push():
            py5.scale(s)
            py5.fill((self.p.area * s * 4) % 255,
                     128,
                     64 + self.filled * 64
                     )
            py5.stroke_weight(1 / s)
            py5.shape(self.shp)

    @staticmethod
    def merge_regions(els):
        num_els = 0
        while num_els !=  len(els):
            num_els = len(els) 
            for a, b in combinations(els, 2):
                if (a in els and b in els and
                    a.isadjacent(b) and a.filled == b.filled):
                    c = Region(cached_union(a.p, b.p), a.filled)
                    els.remove(a)
                    els.remove(b)
                    els.add(c)
        return els

@cache
def cached_union(a, b):
    return unary_union((a, b))

@cache
def cached_polygon(t):
    return Polygon(t)
    

py5.run_sketch(block=False)
