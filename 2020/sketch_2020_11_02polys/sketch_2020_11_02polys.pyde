"""
Possible non-self-intersecting polygons on a grid of points
"""
import pickle

from random import choice, sample, shuffle
from itertools import product, permutations, combinations
from line_geometry import is_poly_self_intersecting, draw_poly, edges_as_sets
add_library('pdf')

DEBUG = False
SIZE, BORDER, HEIGHT = 100, 100, 500
NUM_POINTS = 6
poly_groups = []
reduction = 10
lines_shown = 15
save_pdf = False  # press 'p' to save a PDF
pin_size = 50  # for drawing the points repr.

def setup():
    size(1280, 640)
    create_point_groups()
    # recalc_polys() # press "SHIFT+R"

def draw():
    global save_pdf  # necessário para desligar o 'flag'
    if save_pdf:     # inicia a gravação
        beginRecord(PDF, "####.pdf")
    background(200)
    scale(1. / reduction)
    for line_n in range(len(poly_groups[:lines_shown])):
        pushMatrix()
        translate(0, HEIGHT * line_n)
        for i in range(16):
            # use the first poly from poly_groups to draw pins
            draw_pins(i, poly_groups[line_n][0])
        translate(500, 0)
        for i in range(len(poly_groups[line_n])):
            pushMatrix()
            translate(HEIGHT * i, 0)
            draw_polys(i, poly_groups[line_n])
            popMatrix()
            i += 1
        popMatrix()
    if save_pdf:  # termina a gravação
        endRecord()
        save_pdf = False

def create_point_groups():
    global grid, point_groups
    grid = list(product(range(BORDER, HEIGHT - BORDER + 1, SIZE),
                        range(BORDER, HEIGHT - BORDER + 1, SIZE)))
    naive_point_groups = list(combinations(grid, 6))  # [120::80]]
    control_set = set()
    point_groups = []
    for points in naive_point_groups:
        tp = translated_points(points)
        if tp not in control_set:
            control_set.add(tp)
            point_groups.append(points)
    print("number of 6 point groups:{}".format(len(point_groups)))

def translated_points(points):
        """Return points translated to 0,0"""
        minX = min(x for x, y in points)
        minY = min(y for x, y in points)
        return tuple(sorted((x - minX, y - minY)
                     for x, y in points))

def recalc_polys():
    global grid, point_groups, poly_groups
    poly_groups = [create_polys(points) for points in point_groups]
    poly_groups = [polys for polys in poly_groups if polys]
    print("6 point groups that generated good poly paths:{}".format(len(poly_groups)))

def create_polys(points, no_four_rule=True):
    """
    Generate non-intersecting polygons' from points.
    - check_lines avoids polys with 4 points in a row or col.
    """
    all_polys = list(permutations(points, NUM_POINTS))
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    new_polys = [poly for poly in polys
                if (not no_four_rule or check_lines(poly))
                and not is_poly_self_intersecting(poly)]
    print("non-crossing paths: {}".format(len(new_polys)))
    return list(new_polys)

def check_lines(poly):
    """return False for polys with 4 colinear points."""
    from collections import Counter
    xs = Counter()
    ys = Counter()
    for x, y in poly:
        xs[x] += 1
        ys[y] += 1
    if xs.most_common(1)[0][1] > 3 or ys.most_common(1)[0][1] > 3:
        return False  # polígono ruim, tem line_n ou coluna cheia
    else:
        return True  # polígono bom

def draw_polys(i, polys):
    if i < len(polys):
        fill(0)
        draw_poly(polys[i])

def draw_pins(i, points):
    # resetMatrix()
    noStroke()
    fill(255, 100)
    if grid[i] in points:
        fill(0, 100)
    circle(grid[i][0],
           grid[i][1], pin_size * 2)

def keyPressed():
    global save_pdf
    if key == "p" or key == 'P':
        save_pdf = True
    if key == 'R':
        recalc_polys()

    if key == "s":
        with open("data/poly.data", "wb") as file_out:
            pickle.dump(poly_groups, file_out)
        println("poly groups saved")

    if key == "l":
        with open("data/poly.data", "rb") as file_in:
            saved_project = pickle.load(file_in)
            poly_groups[:] = saved_project
        println("poly groups loaded: {}".format(len(poly_groups)))
        
    if key == "L":
         shuffle(poly_groups)
