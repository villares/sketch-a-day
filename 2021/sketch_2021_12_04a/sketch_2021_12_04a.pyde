# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
1552 triangle pairs with one point in common but no edges in common, on a 3x3 grid
"""

from itertools import product, combinations, permutations
from villares.line_geometry import edges_as_sets

space, border = 60, 60

def setup():
    global tri_combos, W, H, position, num
    size(25 * 60, 10 * 60) # 17 x 16 
    strokeJoin(ROUND)
    grid = product(range(-1, 2), repeat=2)  # 3X3
    # all triple point combinations on a grid
    point_combinations = list(combinations(grid, 3))
    # filter out colinear triples
    triangles = [pts for pts in point_combinations
                 if area(pts) != 0] # removes 3 colinear points
    println("Number of possible triangles: {}".format(len(triangles)))
    all_combos = list(combinations(triangles, 2))
    tri_combos = [(ta, tb) for ta, tb in all_combos
                  if no_same_angles(ta, tb)]
    # tri_combos.sort(key=lambda c: area(c[0]) + area(c[1]))
    println("Number of triangle combinations: {}".format(len(tri_combos)))
    ## Ucomment the following lines to shuffle!
    # from random import shuffle
    # shuffle(tri_combos)
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))

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

def no_same_angles(ta, tb):
    for ea in edges_as_sets(ta):
        for eb in edges_as_sets(tb):
            pa1, pa2 = ea
            aa = int(degrees(atan2(pa1[1] - pa2[1], pa1[0] - pa2[0])))
            pb1, pb2 = eb
            ab = int(degrees(atan2(pb1[1] - pb2[1], pb1[0] - pb2[0])))
            if aa < 0: aa = aa + 180
            if ab < 0: ab = ab + 180
            # print(aa, ab)
            if aa % 180 == ab % 180:
                return False
    return True
        
def draw_combo(n):
    noStroke()
    siz = space / 3
    colors = (color(0, 200, 0), color(0, 0, 200, 128))
    for tri, c in zip(tri_combos[n], colors):
        fill(c)
        (x0, y0), (x1, y1), (x2, y2) = tri[0], tri[1], tri[2]
        triangle(x0 * siz, y0 * siz,
                 x1 * siz, y1 * siz,
                 x2 * siz, y2 * siz)
