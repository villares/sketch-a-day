# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Trying some combinatorics...

add_library('VideoExport')

from random import choice, shuffle, sample
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 5
BORDER = 100
SIZE = 150
RDS = 8
save_frame = True
ensambles = []
st = 0

def setup():
    size(500, 500)
    frameRate(1)
    ensambles[:] = create_points()


def create_points():
    """ non intersecting poly """
    global grid
    good = False
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                   range(BORDER, height - BORDER + 1, SIZE)))
    points = sample(grid, 5)
    combos = set(permutations(points, NUM_POINTS))
    for pts in combos:
        for _ in range(len(pts)-1):
            pts = pts[1:] + (pts[0],)
            combos.discard(pts)
    ens = []
    for pts in combos:
        if not intersecting(pts):
            ens.append(pts) 
    # ens = list(pts)
    print(len(ens))
    shuffle(ens)
    return ens

def draw():
    global st, pts
    background(200)
    scale(1/4.)
    st = -1
    for i in range(4):
        for j in range(4):
            pushMatrix()
            translate(width * i, height * j)  
            st = (st + 1) % len(ensambles)     
            draw_ensamble(ensambles[st])
            popMatrix()

        
def draw_ensamble(pts):   
    # noStroke()
    for i in range(RDS): 
        fill(i * 8, 16)
        r = i * 10
        b_poly_arc_augmented(pts, [r] * NUM_POINTS)

def keyPressed():
    if key == "p":
        saveFrame("####.png")
    if key == " ":
        ensambles[:] = create_points()
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
