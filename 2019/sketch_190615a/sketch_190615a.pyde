# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Trying some combinatorics...

add_library('VideoExport')

from random import choice, shuffle
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 150
RDS = 50
save_frame = True
ensambles = []
st = 0

def setup():
    size(500, 500)
    ensambles[:] = create_points()
    # Video Export
    global ve
    ve = VideoExport(this)
    ve.setFrameRate(20)
    ve.startMovie()

def create_points():
    """ non intersecting poly """
    global grid
    good = False
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                   range(BORDER, height - BORDER + 1, SIZE)))
    combos = permutations(grid, NUM_POINTS)
    ens = []
    for pts in combos:
        if not intersecting(pts):
            ens.append(pts) 
    print(len(ens))
    shuffle(ens)
    return ens

def draw():
    global st, pts
    background(200)

    t = (frameCount % 100) / 100.
    if t == 0:
        st = (st + 1) % len(ensambles)
        # if st == 0:
        #     ve.endMovie()
    
    pts0, pts1 = ensambles[st - 1], ensambles[st]
    pts, rds = [], []
    for i in range(NUM_POINTS):
        pt = lerp(pts0[i][0], pts1[i][0], t), lerp(pts0[i][1], pts1[i][1], t)
        pts.append(pt)
        
    noStroke()
    fill(0, 200, 100)
    # beginShape()
    for i, pt in enumerate(grid):
        ellipse(pt[0], pt[1], 5, 5)
        # text(str(rds[i]), pt[0] + 10, pt[1] + 10)
    # endShape(CLOSE)
    fill(0)
    b_poly_arc_augmented(pts, [RDS] * NUM_POINTS)
    # global save_frame
    if save_frame and frameCount % 2:
        ve.saveFrame()
    #     save_frame = False


def keyPressed():
    if key == "p":
        saveFrame("####.png")
    if key == " ":
        ensambles[:] = create_points()
    # if key == "m":
    #     global save_frame
    #     save_frame = True
    if key == "e":
        ve.endMovie()






def settings():
    """ print markdown to add at the sketc-a-day page"""
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
