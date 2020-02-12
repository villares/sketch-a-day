# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from random import choice, sample, shuffle
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 100
RDS = 50

def setup():
    size(500, 500)
    global ensambles
    ensambles = create_ensambles(create_points(), 30)
    
def create_ensambles(polys, r=1):
    ens = []
    for poly in polys:
        for i in range(64):
            rads = []
            rad_opts = num_to_base(i, 2, 6)
            for c in rad_opts:
                if c == "0":
                    rads.append(-1 * r)
                else:
                    rads.append(1 * r)
            shuffle(rads)
            print(rads)
            ens.append((poly, rads))
    return ens  

def create_points():
    """ non intersecting poly """
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    points = sample(grid, 6)
    total = list(combinations(grid, 6))
    polys = list(permutations(points, NUM_POINTS))
    tested = set()
    for poly in polys[:]:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges) 
        else:
            polys.remove(poly)
    print("inicial: {}".format(len(polys)))
    ni_polys = []
    for poly in polys:
        if not intersecting(poly):
            ni_polys.append(poly) 
    print("sem auto-cruzar: {}".format(len(ni_polys)))
    return list(ni_polys)

def draw():
    background(200)
    # b_poly_arc_augmented(ens, [30] * 6)
    background(200)
    scale(1/16.)
    e = 0
    total = len(ensambles)
    for j in range(16):
        for i in range(16):
            pushMatrix()
            translate(width * i, height * j)  
            if e < total:
                noFill()
                strokeWeight(16)
                b_poly_arc_augmented(ensambles[e][0], ensambles[e][1])
            popMatrix()
            e += 1

def keyPressed():
    if key == "p" or key == 'P':
        saveFrame("####.png")
    if key == ' ':
        ensambles[:] = create_ensambles(create_points(), 30)


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
