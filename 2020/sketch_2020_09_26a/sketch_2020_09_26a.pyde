from random import sample
from itertools import product
from villares import arcs  # github.com/villares/villares

arcs.DEBUG = True
BORDER = 100
SIZE = 100
NUM_POINTS = 10

def setup():
    size(800, 400)
    create_list()

def create_list():
    global p_list, r_list
    radii = [10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40]
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)
    # print('done')

def draw():
    background(210, 200, 200)
    # print(arcs.arc_augmented_poly(p_list, r_list, check_intersection=True))
    stroke(128)
    strokeWeight(10)
    noFill()
    translate(4, 10)
    arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.p_arc, num_points=16)
    filter(BLUR, 6)
    translate(-4, -4)
    strokeWeight(2)
    stroke(0)
    fill(220, 220, 255, 150)
    arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.b_arc)

    strokeWeight(1)
    noFill()
    stroke(0)
    arcs.arc_filleted_poly(p_list, map(abs, r_list), arc_func=arcs.b_arc)


def keyPressed():
    # print('space')
    if key == ' ':
        create_list()
    if key == 's':
        saveFrame('####.png')
