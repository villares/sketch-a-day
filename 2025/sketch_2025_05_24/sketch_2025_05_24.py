"""
Similar to yesterday's sketch, but I removed all dependency of my old awkward
helper functions. I'm now using just shapely and Py5Vector rotation and lerp.
"""

import py5
from py5_tools import animated_gif

from shapely import Polygon, LineString, MultiLineString

pts = [(100, 100), (300, 200), (400, 100), (300, 400), (150, 300)]

def setup():
    global shape_a, shape_b
    py5.size(512, 512)
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))

    a = Polygon(pts)
    external = a.buffer(80)
    hole = external.buffer(-40)
    shape_a =  external - hole
    b = Polygon(list((y, py5.width - x) for x, y, in pts))
    external = b.buffer(60)
    hole = external.buffer(-40)
    shape_b =  external - hole

def draw():
    py5.background(240)
    py5.no_fill()
    py5.stroke(0, 0, 200)
    hatched_poly(
        shape_a,
        angle=py5.radians(py5.frame_count),
        spacing=10
    )
    py5.stroke(0, 200, 0)
    hatched_poly(
        shape_b,
        angle=py5.radians(py5.frame_count) + py5.THIRD_PI,
        spacing=5
    )

def hatched_poly(poly, angle=0, holes=[], spacing=5):
    if not isinstance(poly, Polygon):
        poly = Polygon(poly, holes)
    py5.shape(py5.convert_shape(poly))
    hatch = generate_hatch(poly, angle=angle,spacing=spacing)
    py5.shape(py5.convert_shape(hatch))

def draw_poly(pts, holes=[]):
    py5.shape(py5.convert_cached_shape(Polygon(pts, [hole])))

def generate_hatch(poly, angle=0, spacing=5, holes=[]):
    if not isinstance(poly, Polygon):
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
    py5.save('out.png')

py5.run_sketch(block=False)

