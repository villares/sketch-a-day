from itertools import product
from collections import deque

from shapely.geometry import LineString, LinearRing
import py5
from py5_tools import animated_gif

MARGIN = 64
SPACING = 128 + 64
seed = 11

def setup():
    global grid
    py5.size(512, 512, py5.P3D)
    grid = list(product(range(MARGIN, py5.width, SPACING), repeat=2))
    make_polys()
    py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)
    animated_gif(f'{seed}.gif', duration=0.1, frame_numbers=range(1, 361, 5))
    
def make_polys():
    global poly_a, poly_b
    py5.random_seed(seed)
    poly_a = make_simple_poly(grid)
    poly_b = make_simple_poly(grid)
    
def make_simple_poly(grid, grid_pts= 5):
    simple = False
    while not simple:
        poly = LinearRing(py5.random_sample(grid, grid_pts)).buffer(32).exterior
        simple = poly.is_simple
    return poly
    
def draw():
    py5.background(200)
    py5.translate(256, 256, -256)
    py5.rotate_y(py5.radians(60))
    py5.translate(-256, -256)
    py5.stroke_weight(5)
    #py5.stroke(0, 0, 200)
    #py5.points(grid)
    py5.stroke(255)
    Z_OFFSET = 256
    with py5.push_matrix():
        py5.translate(0, 0, -Z_OFFSET)
        py5.shape(poly_a)
        py5.translate(0, 0, Z_OFFSET * 2)
        py5.shape(poly_b)
    
    py5.stroke(0)
    py5.stroke_weight(1)
    points_a = get_poly_points(poly_a, 60)
    points_b = get_poly_points(poly_b, 60, offset=(90 + py5.frame_count // 6) % 60)
    py5.lines((xa, ya, -Z_OFFSET, xb, yb, Z_OFFSET) for (xa, ya), (xb, yb)
              in zip(points_a, points_b))
    
def get_poly_points(poly, num = 100, offset=0):
    d = poly.length / (num - 1)
    pts = deque((p.x, p.y) for p in
                (poly.interpolate(i * d)
                 for i in range(num)))
    pts.rotate(offset)
    return pts

# from typing import Sequence
# def lerp_sequence(a: Sequence, b: Sequence, t: float) -> Sequence:
#     return tuple(lerp_sequence(ca, cb, t) if isinstance(ca, Sequence)
#                  else py5.lerp(ca, cb, t)             
#                  for ca, cb in zip(a, b))

def key_pressed():
    global seed
    py5.save_frame('###.png')
    seed += 1
    make_polys()

    

py5.run_sketch(block=False)
