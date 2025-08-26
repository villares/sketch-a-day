from itertools import product

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString

shapes = []
grid = list(product(range(64, 512, 128 + 64), repeat=2))   


def setup():
    py5.size(512, 512)
    animated_gif('out.gif', duration=1, frame_numbers=range(1, 21))
    setup_shapes()
    py5.no_loop()
    py5.stroke_join(py5.ROUND)

def setup_shapes(num_shapes=3, buffer=0):
    tri = Polygon()
    while not tri.area:
        shapes.clear()
        pts = py5.random_sample(grid, 3 * num_shapes)#, replace=False)
        if len(set(pts)) < 9:
            continue
        for i in range(0, 3 * num_shapes, 3):
            tri = Polygon(pts[i:i+3])
            if tri.area == 0:
                break
            ang = i // 3 * py5.QUARTER_PI
            shapes.append((0, ang, tri.buffer(buffer)))        
        else:
            continue
            
            
def draw():
    py5.background(200)

    py5.no_fill()
    for c, angle, shp in shapes:
        #py5.stroke(c)
        hatched_poly(
            shp,
            angle=angle,
            spacing=5
            )

def hatched_poly(poly, angle=0, holes=[], spacing=5):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.stroke_weight(3)    
    py5.shape(py5.convert_shape(poly))
    py5.stroke_weight(1)    
    hatch = generate_hatch(poly, angle=angle,spacing=spacing)
    py5.shape(py5.convert_shape(hatch))
    #hatch = generate_hatch(poly, angle=angle + py5.HALF_PI,spacing=spacing)
    #py5.shape(py5.convert_shape(hatch))

def draw_poly(poly, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.shape(py5.convert_cached_shape(poly))

def generate_hatch(poly, angle=0, spacing=5, holes=[]):
    #global p # for debugging
    #p = poly
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    if poly.area == 0:
        return MultiLineString()
    diagonal = py5.dist(*poly.bounds)  # diagonal length
    #print(poly.bounds, diagonal, poly.area)
    num = int(diagonal / spacing)
    V = py5.Py5Vector
    centroid = V(poly.envelope.centroid.x, poly.envelope.centroid.y)
    a = V(-diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    b = V(-diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    c = V(+diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    d = V(+diagonal / 2, +diagonal / 2).rotate(angle) + centroid
#     py5.stroke(255, 0, 0) # for debugging
#     with py5.begin_closed_shape():
#         py5.vertices((a, b, d, c))
#     py5.stroke(0)
    lines = [LineString((V.lerp(a, b, i / num), V.lerp(c, d, i / num)))
             for i in range(num + 1)]
    return MultiLineString(lines).intersection(poly)

def key_pressed():
    #py5.save_frame('###.png')
    setup_shapes()
    py5.redraw()

py5.run_sketch(block=False)

