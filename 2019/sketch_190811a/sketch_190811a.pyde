"""Grid study"""

from random import choice

# add_library('GifAnimation')
# from gif_exporter import gif_export

from grid import Grid

def setup():
    size(500, 500)
    rectMode(CENTER)
    strokeJoin(ROUND)
    strokeWeight(1.5)
    create_grids()
    frameRate(5)
    noStroke()

def create_grids():
    global grids
    grids = []    
    for i in range(20):
        d = int(random(3, 11))  # TODO: rectangular grids
        sp = 20
        x = int(random(-7, 8)) * sp
        y = int(random(-7, 8)) * sp
        si = random(10, 15)
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
        
    # gif_export(GifMaker, filename="sketch_190806a")

def keyPressed():
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        create_grids()
