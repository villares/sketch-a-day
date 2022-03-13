from itertools import product
from random import sample

import py5

from villares.helpers import lerp_tuple

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
    pts.append(sample(grid, num_pts))
    pts.append(sample(grid, num_pts))
    
def draw():
    py5.background(150)
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.translate(w / 2, h / 2, -h / 2)
    py5.rotate_y(py5.radians(py5.frame_count / 10.0))
    py5.translate(-w / 2, -h / 2) 
    for i in range(31):
        t = i / 30.0
        draw_poly(lerp_along_list(pts, t, loop_back=True), t)
    py5.stroke(200, 0, 0)
    py5.stroke_weight(3)
    t = py5.millis() % 4000 / 3999 # remap(mouse_y, 0, height, 0, 1)
    draw_poly(lerp_along_list(pts, t, loop_back=True), t)
        
def draw_poly(pts, t):
    py5.begin_shape()
    for x, y in pts:
        py5.vertex(x, y, py5.lerp(-200, 200, t))
    py5.end_shape(py5.CLOSE)

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