from itertools import product

import py5
import numpy as np
from shapely import LinearRing, GeometryCollection, unary_union


drag = None
W, H = 100, 100
M = 10
N = 8
PTS = np.array([
    [M , M],     
    [M + W, M],     
    [M + W, M + H],     
    [M, M + H],     
])
pts = PTS.copy()

def setup():
    py5.size(600, 600)
 
def draw():
    py5.background(0)
    py5.no_stroke()
    py5.translate(py5.width / 2, py5.height / 2)
    shps = []
    step = int(360 / N)
    for angle in range(0, 360, step):
        a = np.radians(angle)
        R = np.array(((np.cos(a), -np.sin(a)),
                      (np.sin(a),  np.cos(a))
                      ))
        shps.append(LinearRing(pts @ R).buffer(12, join_style='mitre'))
    gc = GeometryCollection(shps)
    py5.fill(200, 100)
    py5.shape(gc)
    
    py5.stroke_weight(10)
    for x, y in pts:
        if mouse_over(x, y):
            py5.stroke(200, 200, 0)
        else:
            py5.stroke(0, 200, 200)
        py5.point(x, y)
  
def mouse_over(x, y, radius=10):
    return py5.dist(
        x, y, py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2) < radius
  
def mouse_pressed():
    global drag
    if drag is None:
        for i, (x, y) in enumerate(pts):
            if mouse_over(x, y):
                drag = i
                break
            
def mouse_dragged():
    if drag is not None:
        m = np.array((py5.mouse_x, py5.mouse_y))
        pm = np.array((py5.pmouse_x, py5.pmouse_y))
        delta =  m - pm 
        pts[drag] += delta 
    
def mouse_released():
    global drag
    drag = None
     
def key_pressed():
    if py5.key == ' ':
        pts[:] = PTS
    
     
py5.run_sketch(block=False)
