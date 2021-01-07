from itertools import product
from random import sample, choice
from villares.line_geometry import line_intersect

MARGIN = 50
SIZE = 100

def setup():
    size(500, 500)
    prepare()    
    
def prepare():
    global points
    n = 12
    grid = list(product(range(MARGIN, width - MARGIN + 1, SIZE), repeat=2))
    points = sample(grid, n)
    

def draw():
    clear()
    for i, pa in enumerate(points[::2]):
        pb = points[i - 1]
        pc = points[i - 2]
        pd = points[i - 3]

        fill(255, 100)
        triangle(pa[0], pa[1],
                 pb[0], pb[1],
                 pc[0], pc[1])
        
    for i, pa in enumerate(points[::2]):
        pb = points[i - 1]
        pc = points[i - 2]
        pd = points[i - 3]
        ip = line_intersect(pa, pb, pc, pd)
        if ip:
            points.append(ip)

def keyPressed():
    print "a"
    prepare()
