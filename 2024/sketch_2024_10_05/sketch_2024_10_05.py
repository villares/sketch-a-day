# ideas... 6 possible modules, 2 x 2 -> 6 ** 4 -> 1296
# But how to sort by "partitions" when same-color regions merge?

from itertools import product, combinations

import py5  # check out https://github.com/py5coding 
from shapely import Polygon

N = 4 # default grid order
MARGIN = 75 # default margin
combos = []

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    start()
    
def start():
    combos.clear()
    # New cell size/scale
    Region.S = (py5.width - MARGIN * 2) / N 
    SQUARE_TYPES = (# diagonal, color a, color b
        (0, 0, 0),  # full black
        (0, 1, 1),  # full white
        (0, 0, 1),  # d1
        (0, 1, 0),  # d2
        (1, 0, 1),  # d3
        (1, 1, 0),  # d4
    )
    squares = [py5.random_choice(SQUARE_TYPES)
               for _ in range(N * N)]
    combos.append(generate_combo(squares))
    
def generate_combo(squares):
    regions = set()
    for (i, j), (t, ca, cb) in zip(product(range(N), repeat=2),
                                   squares):
        if t == 1:
            ra = Region([(i, j), (i + 1, j), (i + 1, j + 1)], color=ca)
            rb = Region([(i, j), (i, j + 1), (i + 1, j + 1)], color=cb)
        else:
            ra = Region([(i, j), (i + 1, j), (i, j + 1)], color=ca)
            rb = Region([(i, j + 1), (i + 1, j), (i + 1, j + 1)], color=cb)           
        regions.update((ra, rb))
    Region.merge_regions(regions)
    return sorted(regions)
    
def draw():
    py5.background(200)
    py5.translate(MARGIN, MARGIN)
    draw_combo(combos[0])
    
def draw_combo(combo):
    for i, r in enumerate(combo):
        r.draw(i)
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        start()


class Region:
    
    S = 225 # default grid cell size
    
    def __init__(self, p, color=0):
        self.p = Polygon(p) if isinstance(p, list) else p
        self.shp = py5.convert_cached_shape(self.p)
        self.shp.disable_style()
        self.color = color
        
    def __repr__(self):
        return f'Region({self.p}, color={self.color})' 
        
    def __eq__(self, other):
        return self.p.area == other.p.area
    
    def __gt__(self, other):
        return self.p.area > other.p.area
    
    def __hash__(self):
        return hash(self.p)
    
    def __add__(self, other):
        if self.color == other.color:
            return Region(self.p.union(other.p),
                          color=self.color)
        else:
            raise TypeError
    
    def isadjacent(self, other):
        return self.p.exterior.overlaps(other.p.exterior)
 
    def draw(self, i=None, s=None):
        s = s or self.S
        with py5.push():
            py5.scale(s)
            # if i is not None:
            #     py5.fill(i * 24, 200, 128 + 64 * (i % 2), 128)
            py5.fill((self.p.area * s) % 255, 128,
                     128 + (32 if self.color == 0 else 96)
                     )
            py5.stroke_weight(2 / s)
            py5.shape(self.shp)
            py5.no_stroke()
            # py5.fill(self.color * 255)
            # py5.circle(self.p.centroid.x, self.p.centroid.y, 30 / s) 

    @staticmethod
    def merge_regions(els):
        num_els = 0
        while num_els !=  len(els):
            num_els = len(els) 
            for a, b in combinations(els, 2):
                if (a in els and b in els and
                    a.isadjacent(b) and a.color == b.color):
                    c = a + b
                    els.remove(a)
                    els.remove(b)
                    els.add(c)
        return els


py5.run_sketch(block=False)