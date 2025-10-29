from itertools import product
from random import sample

import numpy as np
from shapely import unary_union, make_valid
from shapely.geometry import MultiPolygon, Polygon, Point
import py5
import trimesh

import facets # https://github.com/py5coding/python-brasil-2025/blob/main/prototypes/facets.py

bounds = Polygon(((-225, -225), (225, -225), (225, 225), (-225, 225))) 
grid = [(x, y) for x, y in product(range(-225, 226, 75), repeat=2)
        if abs(x)==225 or abs(y)==225
        ]

def setup():
    global max_area
    py5.size(500, 500, py5.P3D)
    py5.color_mode(py5.CMAP, 'viridis_r', 300)
    generate()
    
def generate():
    global result
    pts = py5.random_permutation(grid)
    tp = [(-y, x) for x, y in pts]
    ttp = [(-y, x) for x, y in tp]
    tttp = [(-y, x) for x, y in ttp]
    shapes = MultiPolygon((Polygon(pts), Polygon(tp), Polygon(ttp) , Polygon(tttp)))
    all_shapes = make_valid(shapes)
    negative = make_valid(bounds - all_shapes)
    ap = all_shapes.buffer(-3).buffer(3) 
    nap = negative.buffer(-3).buffer(3) 
    #polys = MultiPolygon([ap]) if isinstance(ap, Polygon) else ap
    polys = MultiPolygon(tuple(ap.geoms) + tuple(nap.geoms))
    max_area = max(shp.area for shp in polys.geoms)
    result = py5.create_shape(py5.GROUP)
    for poly in polys.geoms:
        #         py5.shape(shp)#.difference(shp.buffer(-3))) 
        malha = trimesh.creation.extrude_polygon(poly, 60 - poly.area / max_area * 55)
        py5.fill(poly.area / max_area * 255)
        result.add_child (py5.convert_shape(malha)) #/, min_angle=py5.radians(30)))


def draw():
    py5.background('black')
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(0.7)
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.shape(result)



def key_pressed():
    py5.save_frame('sketch_2025_10_28.png')
    generate()

py5.run_sketch(block=False)

