from itertools import product
from random import sample

import py5

from villares.helpers import lerp_tuple
from villares.line_geometry import is_poly_self_intersecting
from villares.arcs import arc_filleted_poly, arc_augmented_poly

MARGIN = 64
SPACING = 128

pts = []
num_pts = 5

def setup():
    global w, h
    py5.size(512, 512, py5.P3D)
    set_pts()
    py5.no_fill()
    w, h = py5.width, py5.height
    
def set_pts():
    grid = list(product(range(MARGIN, py5.width, SPACING), repeat=2))
    pts[:] = []
    for _ in range(3):
        p = sample(grid, num_pts)
        while is_poly_self_intersecting(p):
            p = sample(grid, num_pts)
        pts.append(p)
    
    
    
def draw():
    py5.background(200)
    py5.stroke(0)
    py5.stroke_weight(2)
    py5.translate(w / 2, h / 2, -h / 2)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.translate(-w / 2, -h / 2) 
    for i in range(31):
        t = i / 30.0
        py5.stroke(0, (i * 16 + py5.frame_count) % 200, 200)
        draw_poly(lerp_along_list(pts, t), t, SPACING / 2)
    py5.stroke(200, 0, 0)
    py5.stroke_weight(3)
#     t = py5.millis() % 4000 / 3999 # remap(mouse_y, 0, height, 0, 1)
#     draw_poly(lerp_along_list(pts, t), t, a=True)
        
def draw_poly(pts, t, r=100, a=False):
    py5.push()
    py5.translate(0, 0, py5.lerp(-200, 200, t))
    arc_filleted_poly(pts, radius=r)
    if a:
        py5.stroke(0, 0, 200)#;arc_augmented_poly(pts)
        py5.begin_shape()
        for x, y in pts:
            py5.vertex(x, y, 5)
        py5.end_shape(py5.CLOSE)
    py5.pop()    

def lerp_along_list(lst, amt, loop_back=False):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = py5.constrain(amt, 0, 1)  # let's play safe
    if loop_back:
        lst = list(lst) + [lst[0]]
    if len(lst) == 1:
        return lst[0]
    cunit = 1.0 / (len(lst) - 1)
    return lerp_tuple(lst[py5.floor(amt / cunit)],
                      lst[py5.ceil(amt / cunit)],
                      amt % cunit / cunit)
def key_pressed():
    if py5.key == ' ':
        set_pts()
        
py5.run_sketch()