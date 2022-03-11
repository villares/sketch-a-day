from itertools import product
from random import sample
from villares.helpers import lerp_tuple

MARGIN = 64
SPACING = 128

pts = []
num_pts = 5

def setup():
    global grid
    size(512, 512)
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    pts.append(sample(grid, num_pts))
    pts.append(sample(grid, num_pts))
    pts.append(sample(grid, num_pts))
    no_fill()
    
def draw():
    background(100)
    stroke(0)
    stroke_weight(1)
    for i in range(31):
        t = i / 30.0
        l_pts = lerp_along_list(pts, t, loop_back=True)
        begin_shape()
        for x, y in l_pts:
            vertex(x, y)
        end_shape(CLOSE)
    stroke(200, 0, 0)
    stroke_weight(3)
    t = millis() % 4000 / 3999 # remap(mouse_y, 0, height, 0, 1)
    l_pts = lerp_along_list(pts, t, loop_back=True)
    begin_shape()
    for x, y in l_pts:
        vertex(x, y)
    end_shape(CLOSE)
        
        
def lerp_along_list(lst, amt, loop_back=False):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if loop_back:
        lst = list(lst) + [lst[0]]
    if len(lst) == 1:
        return lst[0]
    cunit = 1.0 / (len(lst) - 1)
    return lerp_tuple(lst[floor(amt / cunit)],
                      lst[ceil(amt / cunit)],
                      amt % cunit / cunit)
