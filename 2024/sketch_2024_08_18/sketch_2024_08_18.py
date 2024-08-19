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
    pts.append(sample(grid, num_pts))
    pts.append(sample(grid, num_pts))
    background(200)
    stroke(255)
    with begin_closed_shape():
        no_fill()
        vertices(pts[0])
        vertices(pts[1])
    
def draw():
    #background(240)

    time = millis() / 2 % 4000    # count up to 4000 and starts over
    sawtooth_wave = remap(time, 0, 3999, -1, 1) # from -1 to 1, then starts over
    triangle_wave = abs(sawtooth_wave)    # bounces 0-1-0-1-0

    # find our location in 2D path based on 0-1
    the_pts = lerp_sequence(pts[0], pts[1],
                         remap(sin(frame_count / 10), -1, 1, 0, 1))
    x, y = lerp_along_list(triangle_wave, the_pts)
    stroke(0)
    stroke_weight(2)
    point(x, y)    # draw at the location
#     stroke(0)
#     with begin_closed_shape():
#         no_fill()
#         vertices(the_pts)
#         
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