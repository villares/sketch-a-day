from itertools import product
from random import sample

import numpy as np

MARGIN = 64
SPACING = (512 - 128) // 2

num_pts = 4  

def setup():
    global grid
    size(512, 512)
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    start()

def start():
    global pts0, pts1
    s = sample(grid, num_pts * 2)
    pts1 = np.array(s[:num_pts])
    pts0 = np.array(s[num_pts:])    
    background(0)
    stroke(255)
    no_fill()
    stroke_weight(2)
    with begin_closed_shape():
        vertices(pts0)
    with begin_closed_shape():
        vertices(pts1)
    color_mode(HSB)
    
    
def draw():
    for i in range(500):
        sawtooth_wave = remap(i * 2, 0, 999, -1, 1) # from -1 to 1, then starts over
        triangle_wave = abs(sawtooth_wave)    # bounces 0-1-0-1-0
        # find our location in 2D path based on 0-1
        the_pts = lerp(pts0, pts1,remap(cos((frame_count + i) / 10), -1, 1, 0, 1))
        x, y = lerp_along_points(triangle_wave, the_pts)
        stroke(frame_count % 255, 200, 200)
        stroke_weight(2)
        point(x, y)    # draw at the location


def key_pressed():
    if key == 's':
        save_frame('#####.png')
    elif key == ' ':
        start()

def lerp_along_points(amt, pts):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(pts) == 1:
        return pts[0]
    cunit = 1.0 / (len(pts) - 1)
    return lerp(pts[floor(amt / cunit)],
                pts[ceil(amt / cunit)],
                amt % cunit / cunit)

