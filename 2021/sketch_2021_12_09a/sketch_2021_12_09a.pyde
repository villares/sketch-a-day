# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
3 non-intersecting triangles on 6 hexagon vertices: 46
"""

from itertools import product, combinations, permutations
from villares.line_geometry import poly_edges, simple_intersect

space, border = 50, 50

def setup():
    global tri_combos, W, H, position, num
    size(1250, 200)
    strokeJoin(ROUND)
    points = hex_points(0, 0, 1)
    triangles = list(combinations(points, 3))
    all_3tri_combos = list(combinations(triangles, 3))
    tri_combos = [(ta, tb, tc) for ta, tb, tc in all_3tri_combos
                  # if  len(set(ta) | set(tb) | set(tc)) > 4 
                  if not triangle_intersection((ta, tb, tc))
                  ]
    tri_combos.sort(key=lambda c: area(c[0]) - area(c[1]))
    println("Number of triangle combinations: {}".format(len(tri_combos)))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    # tri_combos = [()] + tri_combos # to add a space in the 1st grid position
    background(200)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(tri_combos):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                draw_combo(tri_combos[i])
                popMatrix()
                i += 1

    saveFrame('combos.png')

def hex_points(x, y, tamanho):
    return [(x + tamanho * cos(PI / 180 * 60 * i),
             y + tamanho * sin(PI / 180 * 60 * i))
             for i in range(6)]

def area(p):
   return abs(p[1][0] * (p[2][1] - p[0][1]) +
              p[2][0] * (p[0][1] - p[1][1]) +
              p[0][0] * (p[1][1] - p[2][1]))

def triangle_intersection(ts):
    for t1, t2 in combinations(ts, 2):
        for ea in poly_edges(t1):
            for eb in poly_edges(t2):
                if simple_intersect(shrink(ea), shrink(eb)):
                    return True
    return False

def shrink(seg):
    (xa, ya), (xb, yb) = seg
    new_a = lerp(xa, xb, 0.1), lerp(ya, yb, 0.1)
    new_b = lerp(xa, xb, 0.9), lerp(ya, yb, 0.9)
    return (new_a, new_b)
    
def draw_combo(combo):
    noStroke()
    siz = space / 2.5
    colors = (color(0, 200, 0), color(0, 0, 200, 128), color(200, 0,0, 128), color(240))
    for tri, c in zip(combo, colors):
        fill(c)
        (x0, y0), (x1, y1), (x2, y2) = tri[0], tri[1], tri[2]
        triangle(x0 * siz, y0 * siz,
                 x1 * siz, y1 * siz,
                 x2 * siz, y2 * siz)
