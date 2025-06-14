from itertools import product
from random import sample

MARGIN = 64
SPACING = 128

pts = []
num_pts = 5

def setup():
    global grid
    size(512, 512)
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    pts[:] = sample(grid, num_pts)
    background(200)
    stroke(255)
    with begin_closed_shape():
        no_fill()
        vertices(pts)
    pts[:] = pts + [pts[0]]
    
def draw():
    #background(240)


    t = (frame_count % 100) / 99
        # find our location in 2D path based on 0-1
    x, y = lerp_along_list(t, pts)
    stroke(0)
    stroke_weight(2)
    point(x, y)    # draw at the location

def lerp_along_list(amt, lst):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(lst) == 1:
        return lst[0]
    cunit = 1.0 / (len(lst) - 1)
    return lerp_sequence(lst[floor(amt / cunit)],
                      lst[ceil(amt / cunit)],
                      amt % cunit / cunit)

from typing import Sequence
def lerp_sequence(a: Sequence, b: Sequence, t: float) -> Sequence:
    return tuple(lerp_sequence(ca, cb, t) if isinstance(ca, Sequence)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))