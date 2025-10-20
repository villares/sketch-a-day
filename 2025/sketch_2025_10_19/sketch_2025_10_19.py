# exploring some of Jim's ideas for the Python Brasil tutorial
from itertools import product
from random import sample

import numpy as np
from shapely import unary_union, make_valid
from shapely.geometry import MultiPolygon, Polygon, Point
import py5

grid = list(product(range(-225, 226, 75), repeat=2))

def setup():
    global max_area
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, 'magma_r', 255)
    py5.no_stroke()
    generate()
    
def generate():
    global result    
    shapes = Polygon(py5.random_permutation(grid))
    all_shapes = make_valid(shapes).buffer(-3)
    result = all_shapes.buffer(3)  # .difference(all_shapes.buffer(-4))
    if isinstance(result, Polygon):
        result = MultiPolygon([result])
    
def draw():
    py5.background('black')
    max_area = max(shp.area for shp in result.geoms)
    py5.translate(py5.width / 2, py5.height / 2)
    for shp in result.geoms:
        area = shp.area
        py5.fill(area / max_area * 255)
        py5.shape(shp.difference(shp.buffer(-3))) 

def key_pressed():
    py5.save_frame('####.png')
    generate()

py5.run_sketch(block=False)
