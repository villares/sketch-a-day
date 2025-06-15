from itertools import product

from shapely.geometry import LineString, LinearRing
import py5

poly = LineString([(0, 0), (1, 1), (2, 0), (3, 1)])

MARGIN = 64
SPACING = 128 + 64

def setup():
    global grid
    py5.size(512, 512)
    grid = list(product(range(MARGIN, py5.width, SPACING), repeat=2))
    make_polys()
    
def make_polys():
    global poly_a, poly_b
    py5.background(200)
    simple = False
    poly_a = make_simple_poly(grid)
    poly_b = make_simple_poly(grid)
    
def make_simple_poly(grid, grid_pts = 4):
    simple = False
    while not simple:
        poly = LinearRing(py5.random_sample(grid, grid_pts))
        simple = poly.is_simple
    return poly
    
def draw():
    py5.background(200)
    py5.stroke_weight(2)
    py5.stroke(0, 0, 200)
    py5.points(grid)
    py5.stroke(255)
    py5.shape(poly_a)
    py5.shape(poly_b)
    
    py5.stroke(0)
    py5.stroke_weight(0.5)
    points_a = get_poly_points(poly_a, 200)
    points_b = get_poly_points(poly_b, 200)
    py5.lines((xa, ya, xb, yb) for (xa, ya), (xb, yb)
              in zip(points_a, points_b))
    
def get_poly_points(poly, num = 100):
    d = poly.length / (num - 1)
    return [(p.x, p.y) for p in
            (poly.interpolate(i * d)
             for i in range(num))]

# from typing import Sequence
# def lerp_sequence(a: Sequence, b: Sequence, t: float) -> Sequence:
#     return tuple(lerp_sequence(ca, cb, t) if isinstance(ca, Sequence)
#                  else py5.lerp(ca, cb, t)             
#                  for ca, cb in zip(a, b))

def key_pressed():
    py5.save_frame('###.png')
    make_polys()
    

py5.run_sketch(block=False)
