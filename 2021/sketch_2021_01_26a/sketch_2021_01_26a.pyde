from itertools import product
from random import sample
from villares.line_geometry import par_hatch, draw_poly, is_poly_self_intersecting

BORDER = 100
SIZE = 50

def setup():
    global grid
    size(600, 600)
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))       
    noLoop()
    
def draw():
    background(240)
    points = sample(grid, 4)
    while is_poly_self_intersecting(points):
        points = sample(grid, 4)
        
    strokeWeight(2)
    draw_poly(points)
    strokeWeight(1)
    lines = par_hatch(points, 10, 0, 1)
    for l in lines:
        l.draw()

def keyPressed():
    redraw()
