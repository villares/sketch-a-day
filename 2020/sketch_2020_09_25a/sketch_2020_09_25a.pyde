from random import sample
from itertools import product
from villares import arcs  # github.com/villares/villares

arcs.DEBUG = True
BORDER = 100
SIZE = 150  # try 100!
NUM_POINTS = 6

def setup():
    size(500, 500)
    create_list()

def create_list():
    global p_list, r_list
    radii = [10, 20, 20, 30, 30, 40]
    grid = list(product(range(BORDER, height - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)

def draw():
    background(200)
    # print(arcs.arc_augmented_poly(p_list, r_list, check_intersection=True))
    # stroke(128)
    # strokeWeight(10)
    # arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.p_arc, num_points=4)
 
    strokeWeight(2)
    fill(240, 100)
    arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.b_arc)

    strokeWeight(1)
    noFill()
    arcs.arc_filleted_poly(p_list, map(abs, r_list), arc_func=arcs.b_arc)

 
def keyPressed():
    if key == ' ': create_list()
