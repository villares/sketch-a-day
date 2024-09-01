from itertools import combinations
from functools import lru_cache

import py5
from shapely.geometry import Polygon, GeometryCollection, Point
from shapely.affinity import translate as shapely_translate
from shapely import intersection_all, unary_union

polys = [
    Point((200, 200)).buffer(100),
    Point((300, 200)).buffer(100),
    Point((300, 300)).buffer(100),
    Point((200, 300)).buffer(100),
]

dragged_poly = -1  # no dragged poly

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)

def predraw_update():
    global shp
    rs = get_regions(tuple(polys))
    shp = py5.convert_cached_shape(rs)
    # TODO maybe replace this with a recursive function
    flat_children = []
    if shp.get_child_count():  
        children = shp.get_children()
        for child in children:
            if child.get_child_count():  # there are grandchildren
                flat_children.extend(child.get_children())
            else:
                flat_children.append(child)
    # Change colors
    for i, child in enumerate(flat_children):
        # Py5Shape .contains() for mouse over darkening!
        b = 128 if child.contains(py5.mouse_x, py5.mouse_y) else 255
        child.set_fill(py5.color((i * 18) % 255, 255, b))

def draw():
    py5.background(32, 50, 200)
    py5.shape(shp, 0, 0)

def mouse_pressed():
    global dragged_poly
    for i, p in enumerate(polys):
        if p.contains(Point((py5.mouse_x, py5.mouse_y))):
            dragged_poly = i
            break
            
def mouse_released():
    global dragged_poly
    dragged_poly = -1  # no dragged poly    

def mouse_dragged():
    if dragged_poly >= 0:
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        polys[dragged_poly] = shapely_translate(polys[dragged_poly], dx, dy)
    
@lru_cache(maxsize=64)
def get_regions(polys):
    global regions # for debugging
    regions = []
    n = len(polys)
    for i in range(1, n + 1):
        for combo in combinations(range(n), i):
            intersection = intersection_all([polys[j] for j in combo])
            not_in_combo = unary_union([polys[k] for k in range(n) if k not in combo])
            regions.append(intersection.difference(not_in_combo))
    return GeometryCollection(regions).buffer(-3)

py5.run_sketch(block=False)
