# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
Triangle pairs on a 3x3 grid with with no edge-edge intersections
(some overlapping and some intersections through a vertex).
"""

from itertools import product, combinations, permutations
from villares.line_geometry import poly_edges, simple_intersect

space, border = 25, 25

def setup():
    global tri_combos, W, H, position, num
    size(45 * 25 + 50, 20 * 25 + 50) #16 x 10 
    strokeJoin(ROUND)
    grid = product(range(-1, 2), repeat=2)  # 3X3
    # all triple point combinations on a grid
    point_combinations = list(combinations(grid, 3))
    # filter out colinear triples
    triangles = [pts for pts in point_combinations
                 if area(pts) != 0] # removes 3 colinear points
    all_2tri_combos = list(combinations(triangles, 2))
    tri_combos = [(ta, tb) for ta, tb in all_2tri_combos
                  if  len(set(ta) | set(tb)) > 4 
                  and not triangle_intersection(ta, tb)]
    # tri_combos = [(ta, tb) for i, (ta, tb) in enumerate(tri_combos[:19])  # for debug!
    #               if not same_angles(ta, tb, i)]
    # tri_combos.sort(key=lambda c: c[1])
    tri_combos.sort(key=lambda c: area(c[0]) - area(c[1]))
    println("Number of triangle combinations: {}".format(len(tri_combos)))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    # tri_combos = [()] + tri_combos # to add a space in the 1st grid position
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(tri_combos):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1

    saveFrame('combos.png')

def area(p):
   return abs(p[1][0] * (p[2][1] - p[0][1]) +
              p[2][0] * (p[0][1] - p[1][1]) +
              p[0][0] * (p[1][1] - p[2][1]))

def triangle_intersection(ta, tb, i=None):
    for ea in poly_edges(ta):
        for eb in poly_edges(tb):
            if simple_intersect(shrink(ea), shrink(eb)):
            # if abs(edge_angle(ea) - edge_angle(eb)) < 0.1:
                return True
    return False


def shrink(seg):
    (xa, ya), (xb, yb) = seg
    new_a = lerp(xa, xb, 0.1), lerp(ya, yb, 0.1)
    new_b = lerp(xa, xb, 0.9), lerp(ya, yb, 0.9)
    return (new_a, new_b)

def edge_angle(edge):
        pa, pb = edge
        ea = atan2(pa[1] - pb[1], pa[0] - pb[0])
        return ea + PI if ea < 0 else ea % PI
    
def draw_combo(n):
    noStroke()
    siz = space / 2.5
    colors = (color(0, 200, 0), color(0, 0, 200, 128))
    for tri, c in zip(tri_combos[n], colors):
        fill(c)
        (x0, y0), (x1, y1), (x2, y2) = tri[0], tri[1], tri[2]
        triangle(x0 * siz, y0 * siz,
                 x1 * siz, y1 * siz,
                 x2 * siz, y2 * siz)
