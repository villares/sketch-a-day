from itertools import product
from random import sample, choice
from villares import arcs

MARGIN = 50
SIZE = 100

def setup():
    size(500, 500)
    prepare()

def prepare():
    global triangulos
    n = 12
    grid = list(product(range(MARGIN, width - MARGIN + 1, SIZE), repeat=2))
    pontos = sample(grid, n)
    triangulos = [(pa, pontos[i - 1], pontos[i - 2])
                 for i, pa in enumerate(pontos)]

def subdivide():
    global triangulos
    novos_triangulos = []
    for i, (pa, pb, pc) in enumerate(triangulos):
        mid_ab = midpoint(pa, pb)
        mid_bc = midpoint(pc, pb)
        mid_ac = midpoint(pa, pc)
        novos_triangulos.append((pa, mid_ab, mid_ac))
        novos_triangulos.append((pb, mid_bc, mid_ab))
        novos_triangulos.append((pc, mid_bc, mid_ac))
    triangulos = novos_triangulos

def midpoint(a, b):
    return ((a[0] + b[0]) / 2,
            (a[1] + b[1]) / 2)

def draw():
    clear()
    for t in triangulos:
        # fill(255, 100)
        noFill()
        stroke(255, 100)

        arcs.arc_augmented_poly(t, [10] * 3)

def keyPressed():
    if key == "r":
        prepare()
    elif key == "d":
        subdivide()
