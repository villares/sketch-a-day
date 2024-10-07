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
from shapely import Polygon, unary_union

N = 3 # default grid "order", generates N * N square cells
ensembles = []

def setup():
    # 1296 -> 2 ** 4 + 3 ** 4 -> 16 * 81 -> 48 * 27
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
    SQUARE_TYPES = (0, 1)
    ensembles.clear()
    ensembles[:] = sorted((generate_ensemble(squares) for squares
                       in product(SQUARE_TYPES, repeat=N*N)),
                       key=ensemble_area)
    print(f'Partitions: {len(ensembles)}')
    
def ensemble_area(ensemble):
    """Filled region area"""
    return sum(region.p.area for region in ensemble
               if region.filled)
    
def generate_ensemble(config):
    coords = product(range(N), repeat=2)
    regions = {Region(((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)), filled=fill_type)
               for (i, j), fill_type in zip(coords, config)}
    Region.merge_regions(regions)
    return regions
  
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        start()


class Region:
    
    S = 225 # default grid cell size
    
    def __init__(self, p, filled=True):
        self.p = cached_polygon(p) if isinstance(p, tuple) else p
        # if not isinstance(self.p, Polygon): print(type(self.p)) # No MuliPolygons here!
        self.shp = py5.convert_cached_shape(self.p)
        self.shp.disable_style()
        self.filled = filled
        
    def __repr__(self):
        return f'Region({self.p}, filled={bool(self.filled)})' 
        
    def __eq__(self, other):
        return self.p.area == other.p.area
    
    def __gt__(self, other):
        return self.p.area > other.p.area
    
    def __hash__(self):
        return hash(self.p)
    
    def draw(self, s=None):
        s = s or self.S
        with py5.push():
            py5.scale(s)
            py5.fill((self.p.area * s * 2) % 255,
                     128,
                     160 if self.filled else 64
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
                    isadjacent(a.p, b.p) and a.filled == b.filled):
                    c = Region(cached_union(a.p, b.p), filled=a.filled)
                    els.remove(a)
                    els.remove(b)
                    els.add(c)
        return els

@cache
def cached_union(a_poly: Polygon, b_poly: Polygon) -> Polygon:
    return unary_union((a_poly, b_poly))

@cache
def cached_polygon(t: tuple) -> Polygon:
    return Polygon(t)
    
@cache
def isadjacent(a_poly: Polygon, b_poly: Polygon) -> bool:
    return a_poly.exterior.overlaps(b_poly.exterior)

py5.run_sketch(block=False)
