"""
Code for py5 (py5coding.org) imported mode
"""


from itertools import product
from random import sample


pts = []

drag = None

def setup():
    global grid
    size(880, 600)
    grid = list(product(range(100, width, 200), repeat=2))
    pts[:] = sample(grid, 8)

    
def draw():
    background(240)
    fill(255)
    with begin_shape():
        vertex(*pts[-1])
        for i, p in enumerate(pts):
            if i % 2 == 1:
                c1 = pts[i - 1]
                quadratic_vertex(c1[0], c1[1], pts[i][0], pts[i][1])
            else:
                continue
    for x, y in pts:
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
    for i, (x, y) in enumerate(pts):
        if dist(x, y, mouse_x, mouse_y) < 5:
            drag = i
            return

def mouse_dragged():
    if drag is not None:
        pts[drag] = (mouse_x, mouse_y)
    



    
    
    

