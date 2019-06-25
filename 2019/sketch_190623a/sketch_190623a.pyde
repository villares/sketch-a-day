# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Trying rules by Leopoldo Leal


from random import choice, shuffle, sample
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 100
RDS = 50
ensambles = []

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
    points = sample(grid, NUM_POINTS)
    combos = set(permutations(points, NUM_POINTS))
    for pts in combos:
        for _ in range(len(pts)-1):
            pts = pts[1:] + (pts[0],)
            combos.discard(pts)
            combos.discard(pts[::-1])            
    ens = []
    for pts in combos:
        if not intersecting(pts):
            ens.append(pts) 
    # ens = list(pts)
    print(len(ens))
    shuffle(ens)
    return ens

def draw():
    background(0)
    scale(1/4.)
    st = 0
    for j in range(4):
        for i in range(4):
            pushMatrix()
            translate(width * i, height * j) 
            print st 
            if st < len(ensambles):
                draw_ensamble(ensambles[st])
                st += 1
            popMatrix()

        
def draw_ensamble(pts): 
    noFill()
    stroke(255)
    strokeWeight(4)
    for i in range(8):
        colorMode(HSB)
        stroke(i * 16, 255, 255)
        b_poly_arc_augmented(pts, [i * 10] * NUM_POINTS)
    # for p in pts:
    #     ellipse(p[0], p[1], r * 2 , r * 2)

def keyPressed():
    if key == "p":
        saveFrame("####.png")
    if key == " ":
        background(200)
        ensambles[:] = create_points()


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
