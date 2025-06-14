from itertools import product
from random import sample
from shapely.geometry import LineString

poly = LineString([(0, 0), (1, 1), (2, 0), (3, 1)])



MARGIN = 64
SPACING = 128

grid_pts = 5

def setup():
    global poly
    size(512, 512)
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    poly = LineString(sample(grid, grid_pts))
    background(200)
    stroke(255)
    stroke_weight(2)
    shape(poly)

    
def draw():
    #background(240)

    stroke(0)
    stroke_weight(2)
    num_points = 100
    d = poly.length / (num_points - 1)
    pts = [(p.x, p.y) for p in (poly.interpolate(i * d)
                                for i in range(num_points))]
    points(pts)    # draw at the location

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