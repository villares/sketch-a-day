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
pin_size = 35
selected_pin = -1
points = []

def setup():
    global grid, ensambles
    size(1050, 500)
    grid = list(product(range(BORDER, height - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    ensambles = create_ensambles(create_polys(points))
    # ensambles = create_ensambles(polys)

def draw():
    background(200)
    translate(width / 2 - 25, 0)
    scale(1 / 4.)
    i = 0
    for y in range(4):
        for x in range(4):
            pushMatrix()
            translate(width / 2 * x, height * y)
            fill(0)
            strokeWeight(16)
            draw_ensembles(i)
            popMatrix()
            i += 1
    resetMatrix()
    noStroke()
    fill(255, 100)
    for x, y in grid:
        circle(x, y, pin_size * 2)
    fill(0, 100)
    for x, y in points:
        circle(x, y, pin_size * 2)
    noFill()
    stroke(0)
    strokeWeight(4)
    for i in range(16):
        draw_ensembles(i)

    global selected_pin
    if selected_pin == -2:
        recalc_ensambles()
        selected_pin = -1

def draw_ensembles(i):
    if i < len(ensambles):
        b_poly_arc_augmented(ensambles[i][0], ensambles[i][1])

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


def keyPressed():
    global select_mode
    if key == "p" or key == 'P':
        saveFrame("####.png")
    if key == 'r':
        recalc_ensambles()
    if key == 'R':
        points[:] = sample(grid, NUM_POINTS)
        ensambles[:] = create_ensambles(create_polys(points))
    if key == '=' or key == '+':
        global pin_size
        pin_size += 5
        print("pin_size={}".format(pin_size))
    if key == '-' and pin_size > 10:
        global pin_size
        pin_size -= 5
        print("pin_size={}".format(pin_size))
    if key == 'c':
        pc = calc_polys()

def calc_polys():
    global point_combos, poly_combos
    point_combos = list(combinations(grid, 6))
    poly_combos = dict()
    for combo in point_combos[:10]:
        poly_combos[combo] = create_polys(combo)
        print(len(poly_combos))
    # return poly_combos

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

def mouseReleased():
    global selected_pin
    if selected_pin >= 0:
        pin_x, pin_y = points[selected_pin]
        for pt in grid:
            if dist(pt[0], pt[1], pin_x, pin_y) < pin_size:
                points[selected_pin] = pt
                selected_pin = -2
                return
            else:
                points[selected_pin] = d_pin

def recalc_ensambles():
    if len(points) == NUM_POINTS:
        ensambles[:] = create_ensambles(create_polys(points))
    else:
        print(u"Só vale com {} pinos!".format(NUM_POINTS))

def mousePressed():
    global d_pin, selected_pin
    for i, pt in enumerate(points):
        x, y = pt
        if dist(mouseX, mouseY, x, y) < pin_size:
            d_pin = pt
            selected_pin = i

def mouseDragged():
    if selected_pin >= 0:
        points[selected_pin] = (mouseX, mouseY)
