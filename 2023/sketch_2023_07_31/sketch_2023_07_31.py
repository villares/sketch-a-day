import py5

from shapely import Point, LineString, Polygon
from shapely import MultiPoint, MultiLineString, MultiPolygon
from shapely.ops import unary_union

from villares.shapely_helpers import draw_shapely
# From https://github.com/villares/villares/blob/main/shapely_helpers.py

shapes = []

def setup():
    py5.size(600, 600)
#     ls = LineString(
#         [(100, 50), (100, 200), (200, 50)]
#         )
#     shapes.append(ls.buffer(30))
#     shapes.append(ls)
    #shapes.append(unary_union(random_bars(50, 50, 500, 500)))
    #)
    #mp = MultiPoint([(py5.random(50, 500), py5.random(50, 500)) for _ in range(20)])
    #shapes.append(mp)
    for i in range(5):
        shapes.append(random_bars(50, 50, 500, 500, b=20-i*3))
    
def random_lines(x, y, w, h, n=30):
    return [LineString((py5.random(x, x + w), py5.random(y, y + h)) for _ in range(2)) 
            for _ in range(n)]
    
def random_bars(x, y, w, h, n=30, b=4):
    #return unary_union([l.buffer(b) for l in random_lines(x, y, w, h, n)])
    return MultiLineString(random_lines(x, y, w, h, n)).buffer(b)
    
def draw():
    py5.background(200)
    for i, shps in enumerate(shapes):
        py5.fill(i * 52, 200, 128)
        py5.stroke_weight(3)
        draw_shapely(shps)
    
    
    
py5.run_sketch(block=False)
