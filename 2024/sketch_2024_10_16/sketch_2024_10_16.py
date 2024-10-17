"""

"""

from itertools import product, combinations, permutations
from functools import cache

import py5  # check out https://github.com/py5coding 
from shapely import Polygon, unary_union, MultiPolygon, affinity

COLOR_FACTOR = 60
regions = []

def setup():
    py5.size(600, 600)
    regions.extend((
        Region(
            ((0, 0), (0,1), (1, 1))
            ),
        ))
    for r in regions.copy():
        p = r.p
        for _ in range(3):
            p = affinity.rotate(p, 90) #, origin='centroid')
            minx, miny, maxx, maxy = p.bounds
            p = affinity.translate(p, xoff=-minx, yoff=-miny)
            regions.append(Region(p))
    
    for (x, y), r in zip(product((150, 300), (150, 300)), regions):            
        with py5.push_matrix():
            py5.translate(x, y)
            print(r)
            r.draw(100)
  

def color_maps():
    return {np.array(colors).shape(N, M) for colors in product(MAP_COLORS, repeat=N*M)}
    
def generate_configurations():
    return {generate_configuration(colors.flatten()) for colors in color_maps()}

def generate_configuration(config):
    coords = product(range(N), range(M))
    regions = (Region(((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)), filled=fill_type)
               for (i, j), fill_type in zip(coords, config))
    regions = Region.merge_regions(regions)
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
        p = self.p.copy()
        h = hash(p) #+ hash(self.filled)
        return h

    def __eq__(self, other):
        return self.p.__hash__() == other.__hash__()

    def draw(self, s=None):
        s = s or self.S
        shp = py5.convert_cached_shape(self.p)
        shp.disable_style()
        with py5.push():
            py5.scale(s)
            #py5.fill(self.filled * COLOR_FACTOR, 128, 196)
            py5.fill(((self.p.area) * COLOR_FACTOR) % 255, 128, 196)
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
    # TODO check holes too!
    return a_poly.exterior.overlaps(b_poly.exterior)

py5.run_sketch(block=False)

"""
rotated_polygon = rotate(polygon, angle=angle_in_radians, origin='centroid')
    minx, miny, maxx, maxy = rotated_polygon.bounds
    translated_polygon = translate(rotated_polygon, xoff=-minx, yoff=-miny)

"""
