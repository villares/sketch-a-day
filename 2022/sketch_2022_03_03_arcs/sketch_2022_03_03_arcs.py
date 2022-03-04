from line_geometry import draw_poly   
from random import sample
from itertools import product
import arcs  # github.com/villares/villares

#arcs.DEBUG = True
BORDER = 100
SIZE = 150
NUM_POINTS = 7

def setup():
    size(500, 500)
    create_list()

def create_list():
    global p_list, r_list
    radii = [15, 30, 45] * 3
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)
    # print('done')

def draw():
    background(0, 0, 200)
    stroke(0, 50, 0)
    stroke_weight(3)
    fill(100, 120, 100, 150)
    arcs.arc_augmented_poly(p_list, r_list)
    ptsa = arcs.arc_augmented_poly(p_list, r_list, return_points=True, num_points=6)
    stroke_weight(1)
    no_fill()
    draw_poly(p_list)
    for x, y in ptsa + p_list:
        circle(x, y, 10)
    stroke_weight(3)
    stroke(255)
    arcs.arc_filleted_poly(p_list, map(abs, r_list))
    #ptsb = arcs.arc_filleted_poly(p_list, map(abs, r_list), return_points=True)


def key_pressed():
    # print('space')
    if key == ' ':
        create_list()
    if key == 's':
        save_frame('####.png')