from line_geometry import draw_poly   
from random import sample
from itertools import product
import arcs  # github.com/villares/villares

arcs.DEBUG = True
BORDER = 100
SIZE = 100
NUM_POINTS = 10

def setup():
    size(500, 500)
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
    background(0, 200, 0)
    stroke(0, 50, 0)
    stroke_weight(10)
    no_fill()
    translate(4, 10)
    arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.p_arc, num_points=16)
    apply_filter(BLUR, 4)
    translate(-3, -3)
    stroke_weight(2)
    stroke(0)
    fill(100, 120, 100, 150)
    arcs.arc_augmented_poly(p_list, r_list, arc_func=arcs.b_arc)
    stroke_weight(1)
    no_fill()
    draw_poly(p_list)
    stroke(255)
    arcs.arc_filleted_poly(p_list, map(abs, r_list), arc_func=arcs.b_arc)


def key_pressed():
    # print('space')
    if key == ' ':
        create_list()
    if key == 's':
        save_frame('####.png')