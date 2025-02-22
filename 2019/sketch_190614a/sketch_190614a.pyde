# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

# Testing Video Export library
add_library('VideoExport')

from random import choice
from itertools import product
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 50
# dragged_pt = -1
save_frame = True
ensambles = []
st = 0

def setup():
    size(500, 500)
    for i in range(3):
        ensambles.append(create_points())
    # # Video Export
    # global ve
    # ve = VideoExport(this)
    # ve.setFrameRate(30)
    # ve.startMovie()

def create_points():
    """ non intersecting poly """
    good = False
    grid = product(range(BORDER, width - BORDER + 1, SIZE),
                   range(BORDER, height - BORDER + 1, SIZE))

    while not good:
        pts = []
        for _ in range(NUM_POINTS):
            x, y = 0, 0
            while (x, y) in pts or x == 0:
                x, y = choice(list(grid))
            pts.append((x, y))
        if not intersecting(pts):
            good = True            
    return pts

def draw():
    global st, pts
    background(200)

    t = (frameCount % 500) / 500.
    if t == 0:
        st = (st + 1) % len(ensambles)
        # if st == 0:
        #     ve.endMovie()
    
    pts0, pts1 = ensambles[st - 1], ensambles[st]
    pts, rds = [], []
    for i in range(NUM_POINTS):
        pt = lerp(pts0[i][0], pts1[i][0], t), lerp(pts0[i][1], pts1[i][1], t)
        pts.append(pt)
        

    fill(0, 200, 100)
    beginShape()
    for i, pt in enumerate(pts):
        vertex(pt[0], pt[1])
        # text(str(rds[i]), pt[0] + 10, pt[1] + 10)
    endShape(CLOSE)
    fill(255, 100)
    b_poly_arc_augmented(pts)
    # # global save_frame
    # if save_frame:
    #     ve.saveFrame()
    # #     save_frame = False


def keyPressed():
    if key == "p":
        saveFrame("####.png")
    if key == " ":
        ensambles[:] = []
        for i in range(3):
            ensambles.append(create_points())
    # if key == "m":
    #     global save_frame
    #     save_frame = True
    # if key == "e":
    #     ve.endMovie()






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
