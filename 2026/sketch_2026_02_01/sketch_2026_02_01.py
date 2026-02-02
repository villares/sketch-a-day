from functools import cache

import py5
import numpy as np
from shapely import Polygon

vs = []
shapes = []
areas = []

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, 'viridis')
    start()
    
def start():
    global max_area
    max_area = 1
    vs[:] = (
        np.array(pt) for pt in
        ((0, 0), (py5.width, 0), (py5.width, py5.height), (0, py5.height))
    )
    shapes.clear()
    shapes.append((0, 1, 2, 3))
    
def draw():
    py5.background(0)
    py5.no_fill()
    py5.stroke(0)
    for shp, area in zip(shapes, areas):
        py5.fill(area / max_area)
        with py5.begin_closed_shape():
            py5.vertices(np.array(vs)[np.array(shp)])
        #py5.fill('white')
        #py5.text(int(area), *shape_centroid(shp))
    py5.window_title(str(round(py5.get_frame_rate(), 1)))


def split_shapes():
    new_shapes = []
    while shapes:
        shp = shapes.pop()
        if len(shp) == 4:
            a, b, c, d = shp
            new_shapes.append((a, b, c))
            new_shapes.append((a, c, d))
        elif py5.random(100) < 50:
            a, b, c = shp
            ab = py5.dist(*vs[a], *vs[b])
            bc = py5.dist(*vs[b], *vs[c])
            i = len(vs)
            if ab > bc:
                vs.append((vs[a] + vs[b]) / 2)
                new_shapes.append((a, i, c))
                new_shapes.append((i, b, c))
            elif bc > ab:
                vs.append((vs[b] + vs[c]) / 2)
                new_shapes.append((b, i, a))
                new_shapes.append((i, c, a))               
            else:
                vs.append((vs[a] + vs[c]) / 2)
                new_shapes.append((a, i, b))
                new_shapes.append((i, c, b))
        else:
            new_shapes.append(shp)
    shapes[:] = new_shapes
    areas[:] = (shape_area(shp) for shp in shapes)
    return max(areas)

@cache
def shape_centroid(shp):
    pts = np.array(vs)[np.array(shp)]
    return sum(pts) / len(pts)
  
@cache
def shape_area(shp):
    return pts_area(np.array(vs)[np.array(shp)])
    
def pts_area(pts):
    area = 0.0
    rolled = np.roll(pts, -1, axis=0)
    for (ax, ay), (bx, by) in zip(pts, rolled):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def key_pressed():
    global max_area
    if py5.key == ' ':
        max_area = split_shapes()
    elif py5.key == 'r':
        start()
    elif py5.key == 'p':
        py5.save_frame('###.png')
        
py5.run_sketch(block=False)