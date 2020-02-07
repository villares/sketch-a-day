"""
Possible non self-intersecting quads on 3x3 grid: 94
Number of 2-quad combinations: 4371
Without overlaping points: 191
Cols: 14 Rows: 14
"""

add_library('pdf')
from itertools import product, combinations, permutations
from line_geometry import intersecting

SPACE, BORDER = 40, 10

def setup():
    """Prepare screen or SVG and geometry."""
    global two_quad_combos, quad_pairs, W, H, quads
    size(580, 580)  # used to debug on screen
    strokeJoin(ROUND)
    # Calculate all 3-point combinations on a 3x3 grid
    grid_points = product((-1, 0, 1), repeat=2)
    point_tuples = combinations(grid_points, 4)
    # Identify quads (discard colinear point triples with zero area)
    quads = []
    for pt in point_tuples:
        if not triangle_area(pt[:3]):
            continue
        if not triangle_area((pt[0], pt[1], pt[3])):
            continue
        if not triangle_area((pt[0], pt[2], pt[3])):
            continue
        if not triangle_area((pt[1], pt[2], pt[0])):
            continue
        if not triangle_area((pt[2], pt[0], pt[3])):
            continue
        if not triangle_area(pt[1:]):
            continue
        if not intersecting(pt):
            quads.append(pt)
        if not intersecting((pt[0], pt[2], pt[1], pt[3])):
            quads.append((pt[0], pt[2], pt[1], pt[3]))
        if not intersecting((pt[0], pt[1], pt[3], pt[2])):
            quads.append((pt[0], pt[1], pt[3], pt[2]))
    println("Number of possible non intersecting quads: {}"
            .format(len(quads)))
    # Calculate the 2-quad combinations
    two_quad_combos = list(combinations(quads, 2))
    println("Number of 2-quad combinations: {}"
            .format(len(two_quad_combos)))
    # no superimposing points
    quad_pairs = []
    for t0, t1 in two_quad_combos:
        num_points = len(set(t0 + t1))
        if num_points == 8:
            quad_pairs.append((t0, t1))
    println("Without overlaping points: {}"
            .format(len(quad_pairs)))

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
            if i < len(quad_pairs):
                pushMatrix()
                translate(BORDER + SPACE / 2 + SPACE * x,
                          BORDER + SPACE / 2 + SPACE * y)
                draw_combo(quad_pairs[i], .45)
                popMatrix()
                i += 1
    # exit() # for PDF export()
    noLoop()

def keyPressed():
    saveFrame("frame.png")

def draw_combo(combo, scale_factor=.3):
    """Draw a combination of 2 quads, interpolating 2 others."""
    t0, t3 = combo[0], combo[1]
    t1, t2 = lerp_poly(t0, t3, 0.33), lerp_poly(t0, t3, 0.66)
    quads = (t0, t3)
    # quads = (t0, t1, t2, t3)
    # Colors for the quads
    c0, c3 = color(200, 100, 0), color(0, 100, 100)
    c1, c2 = lerpColor(c0, c3, .33), lerpColor(c0, c3, .66)
    colors = (c0, c3) # (c0, c1, c2, c3)
    # colors = (c0, c1, c2, c3)
    # For each quad, draw it in a different stroke color.
    noFill()
    for t, c in zip(quads, colors):
        stroke(c)
        draw_poly(scale_poly(t, SPACE * scale_factor))


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

def triangle_area(t):
    assert len(t) == 3
    return (t[1][0] * (t[2][1] - t[0][1]) +
            t[2][0] * (t[0][1] - t[1][1]) +
            t[0][0] * (t[1][1] - t[2][1]))
