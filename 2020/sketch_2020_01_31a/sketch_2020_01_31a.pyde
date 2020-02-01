"""
Number of possible triangles: 516
Cols: 43 Rows: 12
"""

add_library('pdf')
from itertools import product, combinations

SPACE, BORDER = 20, 20

def setup():
    """Prepare screen or SVG and geometry."""
    global triangles, W, H
    size(900, 280)  # used to debug on screen
    # size(900, 280, PDF, "43x12.pdf") # export
    strokeJoin(ROUND)
    # Calculate all 3-point combinations on a 4x4 grid
    grid_points = product((-1, 0, 1, 2), repeat=2)
    point_triples = combinations(grid_points, 3)
    # Identify triangles (discard colinear point triples with zero area)
    triangles = []
    for pt in point_triples:
        area = (pt[1][0] * (pt[2][1] - pt[0][1]) +
                pt[2][0] * (pt[0][1] - pt[1][1]) +
                pt[0][0] * (pt[1][1] - pt[2][1]))
        if area != 0:
            triangles.append(pt)
    println("Number of possible triangles: {}"
            .format(len(triangles)))
    # Calculate the display grid dimensions
    W = (width - BORDER * 2) // SPACE
    H = (height - BORDER * 2) // SPACE
    println("Cols: {} Rows: {}"
            .format(W, H))
    global i
    i = 0

def draw():
    """Draw geometry."""
    global i
    background(240)
    for y in range(H):
        for x in range(W):
            if i < len(triangles):
                pushMatrix()
                translate(BORDER + SPACE / 2 + SPACE * x,
                          BORDER + SPACE / 2 + SPACE * y)
                fill(0)
                draw_poly(scale_poly(triangles[i], SPACE * .33))
                popMatrix()
                i += 1
    # exit()
    noLoop()

def keyPressed():
    saveFrame("{}triangles.png".format(len(triangles)))
            

def draw_poly(p_list, closed=True):
    """Draw a polygon from a list of points (vectors or tuples)."""
    beginShape()
    for p in p_list:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()


def lerp_poly(p0, p1, t):
    """Create interpolated version of poly - using tuples for points """
    return [tuple(lerp(c0, c1, t) for c0, c1 in zip(sp0, sp1))
            for sp0, sp1 in zip(p0, p1)]


def scale_poly(p_list, s):
    """Return a scaled version of a list of points (as tuples)."""
    return [(p[0] * s, p[1] * s) for p in p_list]
