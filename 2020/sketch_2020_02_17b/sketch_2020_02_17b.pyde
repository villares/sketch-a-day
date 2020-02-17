"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
Explorando um experimento de geração de formas
proposto por Leopoldo Leal
"""

from random import choice, sample, shuffle
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 100
pin_size = 40
select_mode = True
points = []
reduction = 4

def setup():
    global grid, ensambles
    size(1000, 500)
    grid = list(product(range(BORDER, height - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    points[:] = sample(grid, 6)
    ensambles = create_ensambles(create_polys(points))

def draw():
    background(200)
    translate(500, 0)
    scale(1. / reduction)
    i = 0
    for y in range(reduction):
        for x in range(reduction):
            pushMatrix()
            translate(height * x, height * y)
            draw_ensembles(i)
            popMatrix()
            i += 1
    for i in range(16):
            draw_pins(i)


def create_polys(points):
    """ non intersecting poly """
    all_polys = list(permutations(points, NUM_POINTS))
    tested, polys, ni_polys = set(), [], []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    for poly in polys:
        if not intersecting(poly):
            ni_polys.append(poly)
    print("caminhos sem auto-cruzar: {}".format(len(ni_polys)))
    return list(ni_polys)

def create_ensambles(polys):
    ens = []
    for poly in polys:
        for i in range(2 ** NUM_POINTS):
            rads = []
            rad_opts = num_to_base(i, 2, NUM_POINTS)
            for c in rad_opts:
                if c == "0":
                    rads.append(-1 * pin_size)
                else:
                    rads.append(1 * pin_size)
            ens.append((poly, rads))
    non_crossing_ens = []
    for e in ens:
        crossing = b_poly_arc_augmented(e[0], e[1], check_intersection=True)
        if not crossing:
            non_crossing_ens.append(e)

    print(
        "variantes arredondadas sem auto-cruzar: {}".format(len(non_crossing_ens)))
    return non_crossing_ens

def draw_ensembles(i):
    if i < len(ensambles):
        noFill()
        strokeWeight(8)
        stroke(255)
        b_poly_arc_augmented(ensambles[i][0], ensambles[i][1], b=False)
        stroke(0)
        b_poly_arc_augmented(ensambles[i][0], ensambles[i][1])
        if keyPressed and keyCode == SHIFT:
            for p, r in zip(ensambles[i][0], ensambles[i][1]):
                if r > 0:
                    fill(0, 0, 255)
                else:
                    fill(255, 0, 0)
                noStroke()
                circle(p[0], p[1], 10)

def draw_pins(i):
    resetMatrix()
    noStroke()
    fill(255, 100)
    if grid[i] in points:
        fill(0, 100)
    circle(grid[i][0],
           grid[i][1], pin_size * 2)

def keyPressed():
    global pin_size
    if key == "p" or key == 'P':
        saveFrame("####.png")
    if key == 'r':
        if len(points) == NUM_POINTS:
            ensambles[:] = create_ensambles(create_polys(points))
        else:
            print(u"Só vale com {} pinos!".format(NUM_POINTS))   
    if key == 'R':
        points[:] = sample(grid, NUM_POINTS)
        ensambles[:] = create_ensambles(create_polys(points))
    if key == "=" or key == "+":
        pin_size += 5
    if key == "-" and pin_size > 10:
        pin_size -= 5        

def mouseClicked():
    for p in grid:
        if dist(p[0], p[1], mouseX, mouseY) < pin_size:
            if p in points:
                points.remove(p)
            else:
                points.append(p)


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
