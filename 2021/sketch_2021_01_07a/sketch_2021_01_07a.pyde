from itertools import product
from random import sample, choice
from villares.line_geometry import line_intersect

MARGIN = 50
SIZE = 100

def setup():
    size(500, 500)
    prepare()

def prepare():
    global triangles
    n = 12
    grid = list(product(range(MARGIN, width - MARGIN + 1, SIZE), repeat=2))
    points = sample(grid, n)
    triangles = [(pa, points[i - 1], points[i - 2])
                 for i, pa in enumerate(points)]

def subdivide():
    global triangles
    new_triangles = []
    for i, (pa, pb, pc) in enumerate(triangles):
        mid_ab = midpoint(pa, pb)
        mid_bc = midpoint(pc, pb)
        mid_ac = midpoint(pa, pc)
        new_triangles.append((pa, mid_ab, mid_ac))
        new_triangles.append((pb, mid_bc, mid_ab))
        new_triangles.append((pc, mid_bc, mid_ac))
    triangles = new_triangles

def midpoint(a, b):
    return ((a[0] + b[0]) / 2,
            (a[1] + b[1]) / 2)

def draw():
    clear()
    for pa, pb, pc in triangles:
        fill(255, 100)
        stroke(255, 100)

        triangle(pa[0], pa[1],
                 pb[0], pb[1],
                 pc[0], pc[1])


def keyPressed():
    if key == "r":
        prepare()
    elif key == "d":
        subdivide()
