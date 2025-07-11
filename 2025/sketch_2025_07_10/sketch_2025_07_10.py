from itertools import product
from collections import deque

from shapely.geometry import LineString, LinearRing
import py5
from py5_tools import animated_gif
import numpy as np

MARGIN = 128
SPACING = 128
seed = 1

def setup():
    global grid
    py5.size(512, 512, py5.P3D)
    grid = list(product(range(MARGIN, py5.width, SPACING), repeat=2))
    make_polys()
    py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)
    animated_gif(f'{seed}.gif', duration=0.1, frame_numbers=range(1, 361, 5))
    
def make_polys():
    global poly_a, poly_b, points_a, points_b
    py5.random_seed(seed)
    poly_a = make_simple_poly(grid)
    poly_b = make_simple_poly(grid)
    distances = []
    points_a = get_poly_points(poly_a, 60)
    for i in range(60):
        points_b = get_poly_points(poly_b, 60, offset=i)
        distances.append(total_distance(points_a, points_b))
    min_i = np.argmin(distances)
    points_b = get_poly_points(poly_b, 60, offset=min_i)
    
def make_simple_poly(grid, grid_pts= 6):
    simple = False
    while not simple:
        poly = LinearRing(py5.random_sample(grid, grid_pts)).buffer(50).buffer(-25).exterior
        simple = poly.is_simple
    return poly
    
def draw():
    py5.background(200, 200, 0)
    py5.translate(256, 256, -256)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.translate(-256, -256)
    py5.stroke_weight(6)
    py5.stroke(255)
    
    Z_OFFSET = 256
    with py5.push_matrix():
        py5.translate(0, 0, -Z_OFFSET)
        py5.shape(poly_a)
        py5.translate(0, 0, Z_OFFSET * 2)
        py5.shape(poly_b)
        
    py5.stroke_weight(3)    
    py5.stroke(0)
    py5.no_fill()
    for z in range(-Z_OFFSET + 20, Z_OFFSET, 20):
        t = py5.remap(z, -Z_OFFSET, Z_OFFSET, 0, 1)
        with py5.push_matrix():
            py5.translate(0, 0, z)
#            with py5.begin_closed_shape():
            py5.points(py5.lerp(np.array(points_a), np.array(points_b), t))
#     py5.lines((xa, ya, -Z_OFFSET, xb, yb, Z_OFFSET) for (xa, ya), (xb, yb)
#               in zip(points_a, points_b))

    if py5.frame_count % 60 == 0:
        new_polys()    
    
def total_distance(points_a, points_b):
    distances = np.linalg.norm(np.array(points_a) - np.array(points_b),
                               axis=1)
    return np.sum(distances)
    
def get_poly_points(poly, num = 100, offset=0):
    d = poly.length / (num - 1)
    pts = deque((p.x, p.y) for p in
                (poly.interpolate(i * d)
                 for i in range(num)))
    pts.rotate(offset)
    return pts

def new_polys():
    global seed
    #py5.save_frame('###.png')
    seed += 1
    make_polys()
    

py5.run_sketch(block=False)
