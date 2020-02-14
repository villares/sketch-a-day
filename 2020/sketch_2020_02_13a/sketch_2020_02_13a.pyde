# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from random import choice, sample, shuffle
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 100
RDS = 25
draw_mode = True
points = []

def setup():
    global grid, ensambles
    size(500, 500)
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    points[:] = sample(grid, 6)
    ensambles = create_ensambles(create_polys(points))

def draw():
    background(200)
    scale(1 / 4.)
    i = 0
    for y in range(4):
        for x in range(4):
            pushMatrix()
            translate(width * x, height * y)
            if draw_mode:
                draw_ensembles(i)
            else:
                draw_pins(i)
            popMatrix()
            i += 1

def create_polys(points):
    """ non intersecting poly """
    polys = list(permutations(points, NUM_POINTS))
    tested = set()
    for poly in polys[:]:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
        else:
            polys.remove(poly)
    ni_polys = []
    for poly in polys:
        if not intersecting(poly):
            ni_polys.append(poly)
    print("caminhos sem auto-cruzar: {}".format(len(ni_polys)))
    return list(ni_polys)

def create_ensambles(polys):
    ens = []
    for poly in polys:
        for i in range(64):
            rads = []
            rad_opts = num_to_base(i, 2, 6)
            for c in rad_opts:
                if c == "0":
                    rads.append(-1 * RDS)
                else:
                    rads.append(1 * RDS)
                ens.append((poly, rads))
    non_crossing_ens = []
    for e in ens:
        crossing = b_poly_arc_augmented(e[0], e[1], check_intersection=True)
        if not crossing:
            non_crossing_ens.append(e)

    print(
        "variantes arredondadas sem auto-cruzar: {}".format(len(non_crossing_ens)))
    return non_crossing_ens

def draw_ensembles(e):
    if e < len(ensambles):
        noFill()
        stroke(0)
        strokeWeight(8)
        b_poly_arc_augmented(ensambles[e][0], ensambles[e][1])
        if keyPressed and keyCode == SHIFT:
            for p, r in zip(ensambles[e][0], ensambles[e][1]):
                if r > 0:
                    fill(0, 0, 255)
                else:
                    fill(255, 0, 0)
                noStroke()
                circle(p[0], p[1], 10)

def draw_pins(i):
    if i < 6:
        resetMatrix()
        circle(points[i][0], points[i][1], RDS)


def keyPressed():
    global draw_mode
    if key == "p" or key == 'P':
        saveFrame("####.png")
    if key == ' ':
        if draw_mode:
            draw_mode = False
        else:
            draw_mode = True
    if key == 'r':
        points[:] = sample(grid, 6)
        ensambles[:] = create_ensambles(create_polys(points))


def num_to_base(num, base, pad=0):
    BS = ""
    for i in range(base):
        BS += str(i)
    result = ""
    while num:
        result += BS[num % base]
        num //= base
    while len(result) < pad:
        result = result + "0"
    return result[::-1]
