# Delaunay play
from itertools import product

import py5
from shapely import Polygon
from scipy.spatial import Delaunay
import numpy as np

num_points = 200

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    new_points()
    
def new_points():
    global seed_points, shapely_regions
    W = 60
    R = 20
    seed_points = []
    for i in range(2):
        seed_points.extend((x + (i - 1) * py5.random(-R, R),
                            y + i * py5.random(-R, R)) for x, y
                            in product(range(0, py5.width + W, W),
                                      range(0, py5.height+ W, W)))
    pts = np.array(seed_points)
    tri = Delaunay(seed_points)
    shapely_regions = [Polygon(vs) for vs in pts[tri.simplices]]
    
def draw():
    py5.background(0)
    py5.translate(50, 50)
    py5.scale(500 / 600)
    py5.stroke(0)
    for p in shapely_regions:
        #py5.no_stroke()
        #print(p.area)
        py5.fill(py5.remap(p.area, 250, 2500, 0, 255), 200, 200)
        #py5.fill(16 * len(p.exterior.coords), 200, 200)
        py5.shape(py5.convert_cached_shape(p))
    if py5.is_key_pressed:
        py5.fill(255)
        py5.no_stroke()
        for x, y in seed_points:
            py5.circle(x, y, 5)
    
def key_pressed():
    if py5.key == ' ':
        new_points()
    elif str(py5.key).lower() == 's':
        py5.save_frame('out###.png')
    
            
py5.run_sketch(block=False)
