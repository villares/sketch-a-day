# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# variable radius

add_library('VideoExport')

from random import choice, shuffle, sample
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 150
SIZE = 50
RDS = 50
save_frame = False
ensambles = []
st = 0

def setup():
    size(600, 600, P3D)
    smooth(16)
    ensambles[:] = create_points()
    frameRate(15)
    # Video Export
    global ve
    ve = VideoExport(this)
    ve.setFrameRate(15)
    ve.startMovie()

def create_points():
    """ non intersecting poly """
    global grid
    good = False
    # grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
    #                range(BORDER, height - BORDER + 1, SIZE)))
    # points = sample(grid, NUM_POINTS)
    points = []
    n = 6
    a = TWO_PI / n
    R = width / 2
    for i in range(n):
        x = R + sin(a * i) * R * .5
        y = R + cos(a * i) * R * .5
        points.append((x, y))
    
    combos = set(permutations(points, NUM_POINTS))
    for pts in combos:
        for _ in range(len(pts)-1):
            pts = pts[1:] + (pts[0],)
            combos.discard(pts)
            combos.discard(pts[::-1])            
    ens = []
    for pts in combos:
        # if not intersecting(pts):
            ens.append(pts) 
    # ens = list(pts)
    print(len(ens))
    shuffle(ens)
    return ens

def draw():
    ortho()
    background(250, 250, 240)

    # st = 0
    # scale(1/4.)
    # for j in range(4):
    #     for i in range(4):
    #         pushMatrix()
    #         translate(width * i, height * j) 
    #         translate(height/2, width/2)
    #         rotateY(frameCount / 100.)
    #         # rotateX((frameCount + i * 10 + j * 10) / 50.)
    #         translate(-height/2, -width/2)
    #         if ensambles:
    #             draw_ensamble(ensambles[st])
    #             st = (st + 1) % len(ensambles)
    #         popMatrix()
    translate(height/2, width/2)
    rotateY(frameCount / 100.)
    translate(-height/2, -width/2)

    if save_frame:
        ve.saveFrame()
        if (frameCount - frame_start) / 100. > TWO_PI:
            ve.endMovie()
    
                
def draw_ensamble(pts): 
    noFill()
    stroke(0)
    strokeWeight(4)
    translate(0, 0, -8 * 10)
    for i in range(8):
        # colorMode(HSB)
        strokeWeight(2 + i) # * 1.5)
        translate(0, 0, 20)
        b_poly_arc_augmented(pts, [10 + i * 10] * NUM_POINTS)
        # for p in pts:
        #     ellipse(p[0], p[1], i * 10 , i * 10)

def keyPressed():
    global st, save_frame, frame_start
    if key == "p":
        saveFrame("####.png")
    if key == " ":
        ensambles[:] = create_points()
        st = 0
    if key == "e":
        ve.endMovie()
    if key == "m":
        st += 1
    if key == "s":
        frame_start = frameCount
        save_frame = not save_frame
        println("aave frame: {}".format(save_frame))


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
