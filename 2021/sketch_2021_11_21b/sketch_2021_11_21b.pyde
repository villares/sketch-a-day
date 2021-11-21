# Alexandre B A Villares - https://abav.lugaralgum.com/
# PDF + export code at https://villares.gumroad.com
"""
Number of possible triangles on 3x3 grid: 76
Number of 2-triangle combinations: 2850
Pairs overlapping a single point: 1552
Cols: 97 Rows: 16
"""

from itertools import product, combinations

space, border = 20, 20

def setup():
    size(1980, 360)
    grid = product(range(-1, 2), repeat=2)  # 3X3
    # all triple point combinations on a grid
    points = list(combinations(grid, 3))
    # filter out colinear triples
    triangles = []
    for p in points:
        area = (p[1][0] * (p[2][1] - p[0][1]) +
                p[2][0] * (p[0][1] - p[1][1]) +
                p[0][0] * (p[1][1] - p[2][1]))
        if area != 0:
            triangles.append(p)
    println("Number of possible triangles: {}".format(len(triangles)))
    triangle_combinations = list(combinations(triangles, 2))
    println("Number of triangle combinations: {}".format(len(triangle_combinations)))
    # Remove pairs with superimposing points
    triangle_pairs = [(t0, t1) for t0, t1 in triangle_combinations
                      if len(set(t0 + t1)) == 5]
    println("Pairs overlapping a single point: {}".format(len(triangle_pairs)))     
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    strokeJoin(ROUND)
    # start drawing
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(triangle_pairs):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                draw_pair(triangle_pairs[i])
                popMatrix()
                i += 1

def draw_pair(pair):
    """Draw a pair of 2 triangles, interpolating from one to the other."""
    ta, tb = pair[0], pair[1]
    ca, cb = color(0, 100, 0, 200), color(0, 0, 128, 200)
    half_pair = space * .5  # this size lets the combinations touch
    noStroke()
    fill(ca)
    draw_poly(scale_poly(ta, half_pair))
    fill(cb)
    draw_poly(scale_poly(tb, half_pair))

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

def scale_poly(p_list, s):
    """Return a scaled version of a list of points (as tuples)."""
    return [(p[0] * s, p[1] * s) for p in p_list]
