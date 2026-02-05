from functools import cache

import py5
import numpy as np
from shapely import Polygon

vs = []
shapes = []
areas = []

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.PLASMA)
    start()
    
def start():
    global group
    vs[:] = (
        np.array(pt) for pt in
        ((0, 0), (py5.width, 0), (py5.width, py5.height), (0, py5.height))
    )
    shapes.clear()
    shapes.append((0, 1, 2, 3))
    # this can't be done before setup()...
    group = py5.create_shape(py5.GROUP)  
    
def draw():
    py5.background(0)
    py5.shape(group)
    py5.window_title(str(round(py5.get_frame_rate(), 1)))
    # TODO: try a Py5Shape.GROUP or maybe
    # py5.convert_cached_shape(shapely.MultiPolygon...) ?

def split_shapes():
    global group    
    new_shapes = []
    while shapes:
        shp = shapes.pop()
        if len(shp) == 4:
            a, b, c, d = shp            
            ac = py5.dist(*vs[a], *vs[c])
            bd = py5.dist(*vs[b], *vs[d])
            if ac < bd:
                new_shapes.append((a, b, c))
                new_shapes.append((a, c, d))
            else:
                new_shapes.append((a, b, d))
                new_shapes.append((b, c, d))  
        elif py5.random(100) < 90:
            a, b, c = shp
            abi = len(vs)            
            vs.append((vs[a] + vs[b]) / 2)
            bci = len(vs)            
            vs.append((vs[b] + vs[c]) / 2)
            aci = len(vs)            
            vs.append((vs[a] + vs[c]) / 2)
            new_shapes.append((a, abi, aci))
            new_shapes.append((abi, b, bci, aci))
            new_shapes.append((bci, c, aci))
        else:
            a, b, c = shp
            ab = py5.dist(*vs[a], *vs[b])
            bc = py5.dist(*vs[b], *vs[c])
            i = len(vs)
            if ab > bc:
                vs.append((vs[a] + vs[b]) / 2)
                new_shapes.append((a, i, c))
                new_shapes.append((i, b, c))
            elif bc == ab:
                vs.append((vs[b] + vs[c]) / 2)
                new_shapes.append((b, i, a))
                new_shapes.append((i, c, a))               
            else:
                vs.append((vs[a] + vs[c]) / 2)
                new_shapes.append((a, i, b))
                new_shapes.append((i, c, b))
#         else:
#             new_shapes.append(shp)
    shapes[:] = new_shapes
    areas[:] = (shape_area(shp) for shp in shapes)
    max_area = max(areas)
    
    group = py5.create_shape(py5.GROUP)
    for shp, area in zip(shapes, areas):
        poly = py5.create_shape()
        with poly.begin_closed_shape():
            poly.vertices(np.array(vs)[np.array(shp)])
        poly.set_fill(py5.color(area / max_area))
        group.add_child(poly)
    
  
def shape_area(shp):
    return Polygon(
        np.array(vs)[np.array(shp)]
    ).area
        
def key_pressed():
    if py5.key == ' ':
        split_shapes()
    elif py5.key == 'r':
        start()
    elif py5.key == 'p':
        py5.save_frame('###b.png')
        
py5.run_sketch(block=False)