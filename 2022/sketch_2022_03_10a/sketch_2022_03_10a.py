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
    no_stroke()    
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    pts.append(sample(grid, num_pts))
    pts.append(sample(grid, num_pts))
    background(100)
    
def draw():
   # background(100)
    fill(0)
    for x, y in pts[0]:
        circle(x, y, 32)
    fill(255)
    for x, y in pts[1]:
        circle(x, y, 16)

    time = millis() / 2 % 4000    # count up to 4000 and starts over
    sawtooth_wave = remap(time, 0, 3999, -1, 1) # from -1 to 1, then starts over
    triangle_wave = abs(sawtooth_wave)    # bounces 0-1-0-1-0

    # find our location in 2D path based on 0-1
    the_pts = lerp_tuple(pts[0], pts[1],
                         remap(sin(frame_count / 10), -1, 1, 0, 1))
    x, y = lerp_along_list(triangle_wave, the_pts)
    fill(0, 0, 200)
    ellipse(x, y, 8, 8)    # draw at the location
        
        
def lerp_along_list(amt, lst):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(lst) == 1:
        return lst[0]
    cunit = 1.0 / (len(lst) - 1)
    return lerp_tuple(lst[floor(amt / cunit)],
                      lst[ceil(amt / cunit)],
                      amt % cunit / cunit)