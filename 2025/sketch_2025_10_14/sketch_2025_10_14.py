# exploring some of Jim's ideas for the Python Brasil tutorial

import numpy as np
from shapely import make_valid
from shapely.geometry import MultiPolygon, Point
import py5


circles = [Point(py5.random_int(-5, 5), py5.random_int(-5, 5)).buffer(r) for r in range(10, 221, 12)]
# shuffle the circles so they are not in order
np.random.shuffle(circles)
# combine the circles into a single MultiPolygon
# this will be a jumbled mess and an invalid geometry because of overlapping circles
all_circles = MultiPolygon(circles)

def setup():
    py5.size(500, 500)
    
def draw():
    py5.background('purple')
    py5.translate(250, 250)
    py5.fill(255, 100)
    py5.shape(all_circles) # attempt to visualize circles

def key_pressed():
    global all_circles
    # make_valid applies the even/odd fill rule to correctly determine holes
    # the fact that this works is another reason why shapely is amazing — Jim
    py5.save_frame('####.png')
    all_circles = make_valid(all_circles)

py5.run_sketch()
