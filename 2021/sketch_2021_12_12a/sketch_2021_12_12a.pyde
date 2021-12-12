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
    size(36 * 25 + 50, 29 * 25 + 50) #16 x 10 
    strokeJoin(ROUND)
    grid = product(range(-1, 2), repeat=2)  # 3X3
    # all triple point combinations on a grid
    point_combinations = list(combinations(grid, 3))
    # filter out colinear triples
    triangles = [pts for pts in point_combinations
                 if area(pts) != 0] # removes 3 colinear points
    all_2tri_combos = list(combinations(triangles, 2))
    tri_combos = [(ta, tb) for ta, tb in all_2tri_combos
                  if not triangle_intersection(ta, tb)]
    tri_combos.sort(key=lambda c: -area(c[0]) -area(c[1]))
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
    sta = shrink_tri(ta)
    stb = shrink_tri(tb)
    eas = poly_edges(sta)
    ebs = poly_edges(stb)
    for ea in eas:
        for eb in ebs:
            if simple_intersect(ea, eb):
                return True

    xa, ya = sta[0]
    if point_in_triangle(xa, ya, tb):
        return True            
                
    xb, yb = stb[0]
    if point_in_triangle(xb, yb, ta):
        return True            

    return False

def point_in_triangle(x, y, tri):
    (ax, ay), (bx, by), (cx, cy) = tri
    ab = (x - bx) * (ay - by) - (ax - bx) * (y - by)
    bc = (x - cx) * (by - cy) - (bx - cx) * (y - cy)
    ca = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)
    return (ab < 0) == (bc < 0) == (ca < 0)


def shrink_tri(tri, am=0.1):
    ea, eb, ec = poly_edges(tri)
    sea = shrink(ea, am)
    seb = shrink(eb, am)
    sec = shrink(ec, am)
    a = mid_point(sea[1], seb[0])
    b = mid_point(seb[1], sec[0])
    c = mid_point(sec[1], sea[0])
    return a, b, c
    
def mid_point(a, b):
    (xa, ya), (xb, yb) = a, b
    return (xa + xb) / 2.0, (ya + yb) / 2.0

def shrink(seg, amount=0.1):
    (xa, ya), (xb, yb) = seg
    new_a = lerp(xa, xb, amount), lerp(ya, yb, amount)
    new_b = lerp(xa, xb, 1 - amount), lerp(ya, yb, 1 - amount)
    return (new_a, new_b)

def draw_combo(n):
    noStroke()
    siz = space / 2.5
    colors = (color(0, 200, 0), color(0, 0, 200, 128))
    for tri, c in zip(tri_combos[n], colors):
        tri = shrink_tri(tri, 0.45)
        fill(c)
        (x0, y0), (x1, y1), (x2, y2) = tri[0], tri[1], tri[2]
        triangle(x0 * siz, y0 * siz,
                 x1 * siz, y1 * siz,
                 x2 * siz, y2 * siz)
