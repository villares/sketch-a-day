from itertools import product
from random import sample

import numpy as np

MARGIN = 64
SPACING = 128

num_pts = 4

def setup():
    global grid
    size(512, 512)
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    start()
    
def start():
    global pts0, pts1
    pts1 = np.array(sample(grid, num_pts))
    pts0 = np.array(sample(grid, num_pts))    
    background(200)
    stroke(255)
    with begin_closed_shape():
        no_fill()
        vertices(pts0)
        vertices(pts1)
    color_mode(HSB)
    
    
def draw():
    time = millis() / 2 % 4000    # count up to 4000 and starts over
    sawtooth_wave = remap(time, 0, 3999, -1, 1) # from -1 to 1, then starts over
    triangle_wave = abs(sawtooth_wave)    # bounces 0-1-0-1-0
    # find our location in 2D path based on 0-1
    the_pts = lerp(pts0, pts1,remap(sin(frame_count / 10), -1, 1, 0, 1))
    x, y = lerp_along_list(triangle_wave, the_pts)
    stroke(frame_count % 255, 200, 200)
    stroke_weight(2)
    point(x, y)    # draw at the location


def key_pressed():
    if key == 's':
        save_frame('#####.png')
    elif key == ' ':
        start()

def lerp_along_list(amt, lst):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(lst) == 1:
        return lst[0]
    cunit = 1.0 / (len(lst) - 1)
    return lerp(lst[floor(amt / cunit)],
                      lst[ceil(amt / cunit)],
                      amt % cunit / cunit)
