from itertools import product

import py5
import numpy as np

drag = None
W, H = 100, 100
M = 100
PTS = np.array([
    np.array((M - W, M - H)),     
    np.array((M + W, M - H)),     
    np.array((M + W, M + H)),     
    np.array((M - W, M + H)),     
])
pts = PTS.copy()

def setup():
    py5.size(600, 600)
 
def draw():
    py5.background(0)
    py5.no_fill() 
    py5.stroke_weight(2)
    py5.stroke(255)
    py5.translate(py5.width / 2, py5.height / 2)
    for angle in range(0, 360, 18):
        R = np.array(((np.cos(angle), -np.sin(angle)),
                      (np.sin(angle),  np.cos(angle))))
        with py5.push_matrix(), py5.begin_closed_shape():
             py5.vertices(pts @ R)
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

