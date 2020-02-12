# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

from random import choice, sample, shuffle
from itertools import product, permutations, combinations
from forms import b_poly_arc_augmented
from line_geometry import *

NUM_POINTS = 6
BORDER = 100
SIZE = 100
RDS = 25

def setup():
    size(500, 500)
    global ensambles
    ensambles = create_ensambles(create_points(), RDS)
    
def create_ensambles(polys, r):
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
            # shuffle(rads)
            # print(rads)
            ens.append((poly, rads))
    non_crossing_ens = []
    for e in ens:
       crossing = b_poly_arc_augmented(e[0], e[1], check_intersection=True)
       if not crossing:
          non_crossing_ens.append(e)
          
    print("variantes arredondadas sem auto-cruzar: {}".format(len(non_crossing_ens)))
    return non_crossing_ens  

def create_points():
    """ non intersecting poly """
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    points = sample(grid, 6)
    total = list(combinations(grid, 6))
    print(len(total))
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

def draw():
    background(200)
    # b_poly_arc_augmented(ens, [30] * 6)
    background(200)
    scale(1/4.)
    e = 0
    total = len(ensambles)
    for j in range(4):
        for i in range(4):
            pushMatrix()
            translate(width * i, height * j)  
            if e < total:
                noFill()
                stroke(0)
                strokeWeight(8)
                b_poly_arc_augmented(ensambles[e][0], ensambles[e][1])
                if keyPressed and keyCode == SHIFT:
                    for p, r in zip(ensambles[e][0], ensambles[e][1]):
                        if r > 0: fill(0, 0, 255)
                        else: fill(255, 0, 0)
                        noStroke()
                        circle(p[0], p[1], 10)
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
