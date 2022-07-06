from collections import deque
from random import sample
from itertools import product
from villares.helpers import lerp_tuple, save_png_with_src
import arcs

BORDER = 200
SIZE = 150
NUM_POINTS = 5

drag = None
gestures = [[], []]
rs = 1

def setup():
    size(850, 850, P3D)

def draw():
    background(200)
    translate(width / 2, height / 2, -200)
    rotate_y(frame_count / 100)
    translate(-width / 2, -height / 2)

    stroke_weight(4)
    stroke(0, 0, 100)
    for x, y, z in gestures[0]:
        point(x, y, z)
    stroke(0, 100, 0)
    for x, y, z in gestures[1]:
        point(x, y, z)

    no_fill()
    for i, p1 in list(enumerate(gestures[1])): # [::10]:
        j = floor(remap(i, 0, len(gestures[1]),
                           0, len(gestures[0])))
        p0 = gestures[0][j]
        stroke_weight(0.5)
        stroke(0, 100)
        line(*p0, *p1)
        stroke_weight(2)
        stroke(100, 0, 0)
        lpts = [lerp_tuple(p0, p1, k / 10) for k in range(1, 10)]
        points(lpts)

    if is_mouse_pressed:
        gestures[0].append(gestures[0].popleft())

def key_pressed():
    if key == ' ':
        generate()
    elif key == 's':
        save_png_with_src()
    
def split(pts, d=20):
    if len(pts) == 1:
        return pts
    elif len(pts) > 2:
        return split(pts[:2], d) + split(pts[1:], d)[1:]
    elif dist(*pts[0], *pts[1]) > d:
        return split([pts[0], lerp_tuple(pts[0], pts[1], 0.5), pts[1]], d)
    else:
        return pts

def generate():
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    p_list = sample(grid, NUM_POINTS)
    self_intersecting = arcs.arc_augmented_poly(p_list, radius=100,
                                                  check_intersection=True)
    while self_intersecting:
        p_list = sample(grid, NUM_POINTS)
        self_intersecting = arcs.arc_augmented_poly(p_list, radius=100,
                                  check_intersection=True)
    g0 = arcs.arc_augmented_points(p_list, radius=100, seg_len=20)    
    gestures[0] = deque((x, y, -200) for x, y in split(g0 + g0[:1], 22))

    p_list = sample(grid, NUM_POINTS)
    self_intersecting = arcs.arc_augmented_poly(p_list, radius=100,
                                                  check_intersection=True)
    while self_intersecting:
        p_list = sample(grid, NUM_POINTS)
        self_intersecting = arcs.arc_augmented_poly(p_list, radius=100,
                                  check_intersection=True)
    g1 = arcs.arc_augmented_points(p_list, radius=100, seg_len=12)
    gestures[1] = deque((x, y, 200) for x, y in split(g1 + g1[:1], 16))
    
    if len(gestures[1]) < len(gestures[0]):
       gestures.reverse()
    
