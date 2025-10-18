# exploring some of Jim's ideas for the Python Brasil tutorial

import numpy as np
from shapely import unary_union
from shapely.geometry import MultiPolygon, Polygon, Point
import py5

def setup():
    global max_area
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, 'viridis_r', 255)
    py5.no_stroke()
    generate()
    
def generate():
    global result    
    circles = [
        Point(py5.random_int(-6, 6) * 25,
              py5.random_int(-6, 6) * 25).buffer(py5.random_int(2, 4) * 15)
        for _ in range(20)]
    all_circles = MultiPolygon(circles)
    result = unary_union(circles).difference(all_circles.buffer(-10))
    if isinstance(result, Polygon):
        result = MultiPolygon([result])
    
def draw():
    py5.background('black')
    max_area = max(shp.area for shp in result.geoms)
    py5.translate(250, 250)
    for shp in result.geoms:
        py5.fill(shp.area / max_area * 255)
        py5.shape(shp) 

def key_pressed():
    py5.save_frame('####.png')
    generate()

py5.run_sketch(block=False)
