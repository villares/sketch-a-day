from itertools import combinations
from functools import cache

import py5
from shapely.geometry import Polygon, GeometryCollection, Point

A = Point((200, 200)).buffer(100)
B = Point((300, 200)).buffer(100)
C = Point((300, 300)).buffer(100)
 

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)

def predraw_update():
    global shp
    rs = get_regions((A, B, C))
    shp = py5.convert_cached_shape(rs)
    for i, child in enumerate(shp.get_children()):
        child.set_fill(py5.color(i * 24, 255, 255))

def draw():
    py5.background(100, 100, 200)
    py5.shape(shp, 0, 0)

def mouse_dragged():
    global C
    C = Point((py5.mouse_x, py5.mouse_y)).buffer(100)

py5.run_sketch(block=False)

@cache
def get_regions(polys):
    global regions # for debugging
    regions = []
    n = len(polys)
    for i in range(1, n + 1):
        for combo in combinations(range(n), i):
            intersection = polys[combo[0]]
            for j in combo[1:]:    # get the intersections
                intersection = intersection.intersection(polys[j])
            for k in range(n):
                if k not in combo: # if not part of this combo subtract
                    intersection = intersection.difference(polys[k])            
            if intersection.area:
                regions.append(intersection)
    return GeometryCollection([r.buffer(-5) for r in regions])
