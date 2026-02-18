import py5
import numpy as np
from shapely import Polygon

vs = []
shapes = []
areas = []

def setup():
    py5.size(800, 800, py5.P2D)
    py5.color_mode(py5.CMAP, 'viridis', 255)
    py5.no_stroke()
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
  
def split_shapes():
    global max_area   
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
            continue
        a, b, c = shp
        ab = py5.dist(*vs[a], *vs[b])
        bc = py5.dist(*vs[b], *vs[c])
        ca = py5.dist(*vs[c], *vs[a])
        if ab != bc:
            abi = len(vs)            
            vs.append((vs[a] + vs[b]) / 2)
            bci = len(vs)            
            vs.append((vs[b] + vs[c]) / 2)
            aci = len(vs)            
            vs.append((vs[a] + vs[c]) / 2)
            new_shapes.append((a, abi, aci))
            new_shapes.append((abi, b, bci, aci))
#             new_shapes.append((a, b, bci, aci))            
            new_shapes.append((bci, c, aci))
        else:
            i = len(vs)
            #r = py5.random_int(2)
            if ab > bc:
                vs.append((vs[a] + vs[b]) / 2)
                new_shapes.append((a, i, c))
                new_shapes.append((i, b, c))
            if bc > ab:
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
    group_shape()
    
def distort(intensity=0.0008, f=1.1):
    global scaling_factors, va
    va = np.array(vs)
    va -= np.array((py5.width / 2, py5.height / 2))
    distances = np.linalg.norm(va, axis=1)
    scaling_factors = 1 + (intensity * (distances ** f))
    va =  1.5 * va / scaling_factors[:, np.newaxis]
    va += np.array((py5.width / 2, py5.height / 2))
    vs[:] = va
    group_shape()
    
def group_shape():
    global group
    group = py5.create_shape(py5.GROUP)
    for shp, area in zip(shapes, areas):
        poly = py5.create_shape()
        pts = np.array(vs)[np.array(shp)]
        with poly.begin_closed_shape():
            poly.vertices(pts)
        n = len(pts)
        m = sum(pts) / n
#         cs = [py5.color(255) if n == 3
#               else py5.color(area % 255, 255, 255)
#               for i in range(n)]
#         poly.set_fills(cs)
        poly.set_fill(py5.color(area * n / max_area * 255 / 4))
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
    elif py5.key == 'd':
        distort()
    
        
py5.run_sketch(block=False)