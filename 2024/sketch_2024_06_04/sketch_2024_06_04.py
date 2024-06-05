from itertools import product

import numpy as np

grid_points = list(product(range(-350, 351, 25), repeat=2))

def setup():
    size(800, 800)
    fill(0, 100)
    no_stroke()
    #stroke(255)
    #stroke_weight(2)
    translate(width / 2, height / 2)
    n = len(grid_points)
    w = np.linspace(5, 50, n)
    h = np.linspace(50, 5, n)
    angs = np.linspace(0, TAU, n)
    rect_infos = zip(grid_points, w, h, angs)
    pts = list(map(draw_rect, rect_infos))
    points(pts)
    
def draw_rect(rect_info):
    #print(rect_info)
    pos, w, h, rot = rect_info
    with push_matrix():
        rect_mode(CENTER)
        translate(*pos)
        rotate(rot)
        rect(0, 0, w, h)
    return pos

def key_pressed():
    save('out.png')