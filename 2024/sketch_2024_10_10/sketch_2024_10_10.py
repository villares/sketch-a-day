
from itertools import product, combinations
from functools import cache

import py5  # check out https://github.com/py5coding 
from shapely import Polygon, unary_union

MAP_COLORS = (0, 1, 2, 4)  # because of https://en.wikipedia.org/wiki/Four_color_theorem
COLS, ROWS  = 40, 30
MARGIN = 10
N = 2 #  grid order, N x M subsquares, (N+1) x (M+1) points
M = 2
C_WIDTH = 30  # configuration size
C_HEIGHT = py5.ceil(C_WIDTH / N) * M + 1
C_MARGIN = 2 # internal "configuration" margin
COLOR_FACTOR = 65

configurations = []

def setup():
    py5.size(COLS * C_WIDTH + MARGIN * 2, ROWS * C_HEIGHT + MARGIN * 2)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    m = py5.millis()
    start()
    print(py5.millis() - m)

def start():
    configurations.clear()
    data_path = py5.Path(f'{N}x{M}_polys_triangular_parts.pickle')
    if data_path.is_file():
        polys = py5.load_pickle(data_path)
        configurations[:] = [frozenset(Region(p) for p in p_list) for p_list in polys]    
    else:
        configurations[:] = sorted(generate_configurations(),
                                   key=max_area_min_divisions)
        polys = [[region.p for region in ens] for ens in configurations]
        py5.save_pickle(polys, data_path)
    print(f'Configurations: {len(configurations)}')

def draw():
    py5.background(0)
    py5.translate(MARGIN, MARGIN)
    Region.S = (C_WIDTH - C_MARGIN * 2) / N  # size of subsquare
    k = 0      
    for i in range(ROWS):
        y = i * C_HEIGHT
        for j in range(COLS):
            x = j * C_WIDTH  
            if k < len(configurations):
                draw_configuration(
                    configurations[k],
                    x + C_MARGIN,
                    y + C_MARGIN)
            k += 1
    
def draw_configuration(configuration, xe, ye):
    with py5.push_matrix():
        py5.translate(xe, ye)
        for region in configuration:
            region.draw()
 

 
def max_area_min_divisions(configuration):
    return max(region.p.area for region in configuration) - len(configuration) / 10
 
def generate_configuration(type_and_colors):
    coords = product(range(N), range(M))
    regions = set()
    for (i, j), (t, ca, cb) in zip(coords, type_and_colors):
        if ca == cb:
            rab = Region(((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)), filled=ca)
            regions.add(rab)
        else:
            if t == 1:
                ra = Region(((i, j), (i + 1, j), (i + 1, j + 1)), filled=ca)
                rb = Region(((i, j), (i, j + 1), (i + 1, j + 1)), filled=cb)
            else:
                ra = Region(((i, j), (i + 1, j), (i, j + 1)), filled=ca)
                rb = Region(((i, j + 1), (i + 1, j), (i + 1, j + 1)), filled=cb)           
            regions.update((ra, rb))
    Region.merge_regions(regions)
    return frozenset(regions)

#     
#     regions = {Region(((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)), filled=fill_type)
#                for (i, j), fill_type in zip(coords, config)}
#     regions = Region.merge_regions(regions)
#     return frozenset(regions)

def generate_configurations():
    type_and_colors = product((0, 1), MAP_COLORS, MAP_COLORS)
    return set(generate_configuration(tcs) for tcs in product(type_and_colors, repeat=N*M))



def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')


class Region:
    
    S = 225 # default grid cell size
    
    def __init__(self, p, filled=0):
        self.p = cached_polygon(p) if isinstance(p, tuple) else p
        #if not isinstance(self.p, Polygon): print(type(self.p)) # No MuliPolygons here!
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
        return hash(self.p)
    
    def draw(self, s=None):
        s = s or self.S
        with py5.push():
            py5.scale(s)
            py5.fill((self.p.area * COLOR_FACTOR) % 255, 128, 196)
            py5.stroke_weight(1 / s)
            py5.shape(self.shp)
            py5.no_stroke()


    @staticmethod
    def merge_regions(els):
        num_els = 0
        while num_els !=  len(els):
            num_els = len(els) 
            for a, b in combinations(els, 2):
                if (a in els and b in els and
                    isadjacent(a.p, b.p) and a.filled == b.filled):
                    c = Region(cached_union(a.p, b.p), a.filled) 
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


