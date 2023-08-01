import py5

from shapely import Point, LineString, Polygon
from shapely import MultiPoint, MultiLineString, MultiPolygon
from shapely.ops import unary_union
# From https://github.com/villares/villares/blob/main/shapely_helpers.py
from villares.shapely_helpers import draw_shapely

shapes = []

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    for i in range(5):
        shapes.append(random_bars(50, 50, 500, 500, b=20-i*3))
    
def random_lines(x, y, w, h, n=30):
    return [LineString((py5.random(x, x + w), py5.random(y, y + h)) for _ in range(2)) 
            for _ in range(n)]
    
def random_bars(x, y, w, h, n=30, b=4):
    return MultiLineString(random_lines(x, y, w, h, n)).buffer(b)
    
def draw():
    py5.background(200)
    for i, shps in enumerate(shapes):
        py5.fill(i * 52, 200, 128)
        py5.stroke_weight(3)
        draw_shapely(shps)
    
def key_pressed():
    py5.save('out.png')
    
py5.run_sketch(block=False)
