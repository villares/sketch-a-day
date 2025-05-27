from itertools import product

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString

shapes = []

def setup():
    py5.size(512, 512)
    py5.no_smooth()
    animated_gif('out.gif', duration=2, frame_numbers=range(1, 17))
    setup_shapes()
    py5.no_loop()
    py5.stroke_join(py5.ROUND)

def setup_shapes():
    shapes.clear()
    grid = list(product(range(128, 512, 128), repeat=2))   
    for i, c in enumerate((255, 255, 255)): #, 'green', 'blue')):
        pts = py5.random_sample(grid, 5, replace=False)
        a = Polygon(pts)
        simple = a.buffer(-1)
        hole = simple.buffer(5)
        external = hole.buffer(40)
        shape_a =  external - hole
        ang = i * py5.THIRD_PI + py5.QUARTER_PI
        shapes.append((shape_a, c, ang, a))
            
def draw():
    py5.background(0, 0, 150)
    py5.stroke_weight(5)
    for *_, polys in shapes:
        py5.fill(0, 32)
        py5.no_stroke()
        py5.stroke(0, 0, 64)
        draw_poly(polys)
        
    py5.no_fill()
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
    py5.stroke_weight(1)    
    hatch = generate_hatch(poly, angle=angle,spacing=spacing)
    py5.shape(py5.convert_shape(hatch))
    hatch = generate_hatch(poly, angle=angle + py5.HALF_PI,spacing=spacing)
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
    #py5.save_frame('###.png')
    setup_shapes()
    py5.redraw()

py5.run_sketch(block=False)

