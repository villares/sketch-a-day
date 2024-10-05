# ideas... 6 possible modules, 2 x 2 -> 6 ** 4 -> 1296
# But how to sort by "partitions" when same-color regions merge?

from itertools import product, combinations

import py5  # check out https://github.com/py5coding 
from shapely import Polygon, MultiPolygon
N = 2 # grid 2 x 2
QUADRANT_TYPES = (
    (0, 0, 0),     # full black
    (0, 255, 255), # full white
    (0, 0, 255),  # d1
#     (0, 255, 0),  # d2
    (1, 0, 255),  # d3
#    (1, 255, 0),  # d4
    )

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    
def start():
    quadrants = [py5.random_choice(QUADRANT_TYPES)
                 for _ in range(N * N)]
    regions = set()
    for (i, j), (t, ca, cb) in zip(product(range(2), repeat=2),
                                   quadrants):
        if t == 1:
            ra = Region([(i, j), (i + 1, j), (i + 1, j + 1)], color=ca)
            rb = Region([(i, j), (i, j + 1), (i + 1, j + 1)], color=cb)
        else:
            ra = Region([(i, j), (i + 1, j), (i, j + 1)], color=ca)
            rb = Region([(i, j + 1), (i + 1, j), (i + 1, j + 1)], color=cb)           
        regions.update((ra, rb))
    Region.merge_regions(regions)
    Region.elements = regions
    
def draw():
    py5.background(200)    
    Region.grid(4)
    #py5.translate(-4, -4) 
    for i, r in enumerate(sorted(Region.elements)):
        #py5.translate(2, 2) # debug!
        r.draw(i)
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        start()


            
#@functools.total_ordering
class Region:
    
    M = 75 # margin    
    S = 225 #(py5.width - M * 2) / N # scale
    elements = {}
    
    def __init__(self, p, color=0):
        self.p = Polygon(p) if isinstance(p, list) else p
        self.shp = py5.convert_cached_shape(self.p)
        self.shp.disable_style()
        self.color = color
        
    def __repr__(self):
        return f'Region({self.p}, color={self.color})' 
        
#     def __eq__(self, other):
#         return self.area == other.area
    
    def __gt__(self, other):
        return self.p.area > other.p.area
    
    def __hash__(self):
        return hash(self.p)
    
    def __add__(self, other):
#        if self.color == other.color and self.isadjacent(other):
        if self.color == other.color:
            return Region(self.p.union(other.p),
                          color=self.color)
        else:
            raise TypeError
    
    def isadjacent(self, other):
        return self.p.exterior.overlaps(other.p.exterior)
 
    def draw(self, i=None):
        with py5.push():
            py5.scale(self.S)
            py5.fill(self.color, 128)
            py5.no_stroke()
            if i is not None:
                py5.fill(i * 24, 200, 128 + 64 * (i % 2), 128)
                #py5.stroke_weight(1 / self.S)
            py5.shape(self.shp)
            py5.fill(self.color)
            py5.circle(self.p.centroid.x,
                       self.p.centroid.y,  
                       30/150)
        
    @classmethod
    def grid(cls, n, m=None):
        cls.GRID = list(product(range(n), range(m or n)))
        py5.translate(cls.M, cls.M)
        py5.stroke(0)
        py5.stroke_weight(5)
        py5.points((x * cls.S, y * cls.S)
                   for x, y in cls.GRID)

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


py5.run_sketch(block=False)
        
        






