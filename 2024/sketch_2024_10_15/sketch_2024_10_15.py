"""
2811 ways of coloring a grid of 3 x 3 squares removing rotations,
"""

from itertools import product, combinations, permutations
from functools import cache

import py5  # check out https://github.com/py5coding 
from shapely import Polygon, unary_union, MultiPolygon
import numpy as np

MAP_COLORS = (0, 1, 2, 4)  # because of https://en.wikipedia.org/wiki/Four_color_theorem
COLS, ROWS  = 74, 38
MARGIN = 20
N = 3 #  grid order, N x M subsquares, (N+1) x (M+1) points
M = 3
C_WIDTH = 22  # configuration size
C_HEIGHT = py5.ceil(C_WIDTH / N) * M + 1
C_MARGIN = 2 # internal "configuration" margin
COLOR_FACTOR = 40

configurations = []

def setup():
    py5.size(COLS * C_WIDTH + MARGIN * 2, ROWS * C_HEIGHT + MARGIN * 2)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    start()

def start():
    start_time = py5.millis()
    configurations.clear()
    data_path = py5.Path(f'{N}x{M}-new.pickle')
    existing_pickle = data_path.is_file()
    if existing_pickle:
        configs = py5.load_pickle(data_path)
        configs = {frozenset(Region.merge_regions(regions)) for regions in configs}
    else:
        configs = generate_configurations()
        py5.save_pickle(configs, data_path)
    configurations[:] = sorted(configs, key=num_colors_max_area)
    delta_time = py5.millis() - start_time
    print(f'{len(configurations)} configurations.')
    print(f'shown on a {COLS} x {ROWS} grid of {COLS*ROWS} positions.')
    message = 'load data from disk' if existing_pickle else 'generate'
    print(f'{delta_time} milliseconds to {message}.')

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
    
def draw_configuration(config, xe, ye):
    with py5.push_matrix():
        py5.translate(xe, ye)
        for region in config:
            region.draw()

def color_maps():
    return {ColorArray(colors, N, M) for colors in product(MAP_COLORS, repeat=N*M)}
    
def generate_configurations():
    return {generate_configuration(colors) for colors in color_maps()}

def generate_configuration(config):
    coords = product(range(N), range(M))
    regions = (Region(((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)), filled=fill_type)
               for (i, j), fill_type in zip(coords, config))
    #regions = Region.merge_regions(regions)
    #return frozenset(Region(r.p) for r in regions)
    #return frozenset(Region(r.p, filled=0) for r in regions)
    return frozenset(regions)
    
def num_colors_max_area(config):
    return (
        len(set(r.filled for r in config)) * 100    
         - sum(r.p.area for r in config) / len(config)
        )

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')

class ColorArray:
    def __init__(self, colors, N, M):
        self._array = np.array(colors)
#         values, inverse_indices = np.unique(array, return_inverse=True)
#         self._array = np.array(inverse_indices).reshape(N,M)
        
    def __hash__(self):
        a = self._array
        h = hash(tuple(a.flatten()))
        values, inverse_indices = np.unique(a, return_inverse=True)
        for vs in permutations(MAP_COLORS, len(values)):
            a = np.array(vs)[inverse_indices].reshape(M,N)
            h = min(h, hash(tuple(a.flatten())))
            for _ in range(3):
                    a = np.rot90(a, 1)                    
                    h = min(h, hash(tuple(a.flatten())))
        return h

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __iter__(self):
        return iter(self._array.flatten())
      
class Region:
    
    S = 225 # default grid cell size
    
    def __init__(self, p, filled=0):
        self.p = cached_polygon(p) if isinstance(p, tuple) else p
        self.filled = filled
        
    def __repr__(self):
        return f'Region({self.p}, filled={self.filled})' 
        
    def __gt__(self, other):
        return self.p.area > other.p.area
    
    def __hash__(self):
        return hash(self.p) + hash(self.filled)

    def __eq__(self, other):
        return self.p.__hash__() == other.__hash__()

    def draw(self, s=None):
        s = s or self.S
        shp = py5.convert_cached_shape(self.p)
        shp.disable_style()
        with py5.push():
            py5.scale(s)
            py5.fill(self.filled * COLOR_FACTOR, 128, 196)
            #py5.fill(((self.p.area) * COLOR_FACTOR) % 255, 128, 196)
            py5.stroke_weight(1 / s)
            #py5.no_stroke()
            py5.shape(shp)

    @staticmethod
    def merge_regions(regions):
        els = set(regions)
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


