from random import sample
from itertools import product
from villares.helpers import lerp_tuple, save_png_with_src
from villares import arcs


BORDER = 200
SIZE = 150
NUM_POINTS = 5

drag = None
gestures = ([], [])
rs = 1

def setup():
    size(850, 850)

def draw():
    background(200)
#     stroke(255)
#     stroke_weight(2)
#     if gestures[0]:
#         with begin_closed_shape():
#             vertices(gestures[0])
#     if gestures[1]:
#         with begin_closed_shape():
#             vertices(gestures[1])
    no_stroke()
    fill(0, 0, 100)
    for x, y in gestures[0]:
        circle(x, y, 4)
    fill(0, 100, 0)
    for x, y in gestures[1]:
        circle(x, y, 4)
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
    p_list = sample(grid, NUM_POINTS * 2)
    g0 = arcs.arc_augmented_points(p_list[:NUM_POINTS], radius=100, num_points=16)    
    gestures[0][:] = split(g0 + g0[:1], 15) 
    g1 = arcs.arc_augmented_points(p_list[NUM_POINTS:], radius=100, num_points=16)
    gestures[1][:] = split(g1 + g1[:1], 15)
    if len(gestures[1]) < len(gestures[0]):
        g0 = gestures[0][:]
        g1 = gestures[1][:]
        gestures[1][:], gestures[0][:] = g0, g1
    
    
