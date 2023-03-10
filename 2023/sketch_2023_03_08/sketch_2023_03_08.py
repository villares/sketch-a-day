"""
Code for py5 (py5coding.org) imported mode
"""

from itertools import product
from random import sample

drag = None

handles = []

def setup():
    global grid
    size(800, 800)
    grid = list(product(range(100, width, 200), repeat=2))
    handles[:] = sample(grid, 8)
    
def draw():
    background(240)
    pts = []
    for i, b in enumerate(handles):
        a = handles[i - 1]
        m = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 
        pts.append(m)
        pts.append(b)
    
    fill(255)
    with begin_shape(POLYGON):
        vertex(*pts[-2])
        for i, p in enumerate([pts[-1]] + pts, -1):
            if i % 2 == 0:
                c1 = pts[i - 1]
                quadratic_vertex(c1[0], c1[1], pts[i][0], pts[i][1])
            else:
                continue
    for x, y in handles:
        if dist(x, y, mouse_x, mouse_y) < 5:
            fill(255, 0, 0)
        else:
            no_fill()
        circle(x, y, 10)
        
def mouse_released():
    global drag
    drag = None
    
    
def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(handles):
        if dist(x, y, mouse_x, mouse_y) < 5:
            drag = i
            return

def mouse_dragged():
    if drag is not None:
        handles[drag] = (mouse_x, mouse_y)
    



    
    
    
