"""Grid study"""

from random import choice

from grid import Grid

def setup():
    size(500, 500)
    rectMode(CENTER)
    colorMode(HSB)
    strokeJoin(ROUND)
    strokeWeight(2)
    create_grids()
    frameRate(5)

def create_grids():
    global grids
    grids = []    
    for i in range(10):
        d = int(random(4, 11))
        sp = 20
        x = int(random(-7, 8)) * sp
        y = int(random(-7, 8)) * sp
        si = random(15, 35)
        sh = choice((ELLIPSE, ELLIPSE, RECT, RECT, TRIANGLE, TRIANGLES))
        grids.append(Grid(pos=(x, y),
                           dims=(d, d),
                           space=sp,
                           elem=(sh, si))
                      )
def draw():
    background(240)
    translate(width / 2., height / 2.)
    # scale(.5, .5)
    
    for g in grids:
        g.update()

def keyPressed():
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        create_grids()
