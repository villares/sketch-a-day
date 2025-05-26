from itertools import product

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString

shapes = []

def setup():
    py5.size(512, 512)
    #animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))
    setup_shapes()
    py5.no_loop()

def setup_shapes():
    shapes.clear()
    grid = list(product(range(128, 512, 128), repeat=2))   
    for i, c in enumerate((0, 0, 0)): #, 'green', 'blue')):
        pts = py5.random_sample(grid, 5, replace=False)
        a = Polygon(pts)
        simple = a.buffer(0)
        hole = simple.buffer(40)
        external = simple.buffer(80)
        shape_a =  external - hole
        ang = i * py5.THIRD_PI + py5.QUARTER_PI
        shapes.append((shape_a, c, ang, simple))
            
def draw():
    py5.background(240)
    py5.no_fill()
    py5.stroke_weight(5)
    for *_, polys in shapes:
        py5.stroke(255)
        draw_poly(polys)
    for shp, c, angle, _ in shapes:
        py5.stroke(c)
        hatched_poly(
            shp,
            angle=angle,
            spacing=5
            )

def hatched_poly(poly, angle=0, holes=[], spacing=5):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.stroke_weight(2)    
    py5.shape(py5.convert_shape(poly))
    hatch = generate_hatch(poly, angle=angle,spacing=spacing)
    py5.stroke_weight(1)    
    py5.shape(py5.convert_shape(hatch))

def draw_poly(poly, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.shape(py5.convert_cached_shape(poly))

def generate_hatch(poly, angle=0, spacing=5, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    diagonal = py5.dist(*poly.bounds)  # diagonal length
    num = int(diagonal / spacing)
    V = py5.Py5Vector
    centroid = V(poly.centroid.x, poly.centroid.y)
    a = V(-diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    b = V(-diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    c = V(+diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    d = V(+diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    lines = [LineString((V.lerp(a, b, i / num), V.lerp(c, d, i / num)))
             for i in range(num + 1)]
    return MultiLineString(lines).intersection(poly)

def key_pressed():
    py5.save_frame('###.png')
    setup_shapes()
    py5.redraw()

py5.run_sketch(block=False)

