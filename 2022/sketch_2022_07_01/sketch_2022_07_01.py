from random import sample
from itertools import product
from villares.helpers import lerp_tuple
from villares import arcs

BORDER = 200
SIZE = 150
NUM_POINTS = 6

drag = None
gestures = ([], [])

def setup():
    size(850, 850)

def draw():
    background(200)
    stroke(255)
    stroke_weight(1)
    if gestures[0]:
        with begin_closed_shape():
            vertices(gestures[0])
    if gestures[1]:
        with begin_closed_shape():
            vertices(gestures[1])
    no_stroke()
    fill(0, 0, 100)
    for x, y in gestures[0]:
        circle(x, y, 5)
    fill(0, 100, 0)
    for x, y in gestures[1]:
        circle(x, y, 5)
    no_fill()
    for i, p1 in list(enumerate(gestures[1])): # [::10]:
        j = floor(remap(i, 0, len(gestures[1]),
                           0, len(gestures[0])))
        p0 = gestures[0][j]
        lpts = [lerp_tuple(p0, p1, k / 10) for k in range(11)]
        stroke_weight(0.5)
        stroke(0, 100)
        line(*p0, *p1)
        stroke_weight(3)
        stroke(100, 0, 0)
        points(lpts[1:-1])

def key_pressed():
    if key == ' ':
        generate()
    elif key == 's':
        save_frame('###.png')
    
def generate():    
    radii = [100] * 8 + [50] * 2
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)
    gestures[0][:] = arcs.arc_augmented_points(p_list, r_list, num_points=16)
    r_list = sample(radii, NUM_POINTS)
    p_list = sample(grid, NUM_POINTS)
    gestures[1][:] = arcs.arc_augmented_points(p_list, r_list, num_points=16)

# def mouse_dragged():
#     if drag is not None:
#         gestures[drag].append((mouse_x, mouse_y))
# 
# def mouse_pressed():
#     global drag
#     if len(gestures[0]) == 0:
#         drag = 0
#     elif len(gestures[1]) == 0:
#         drag = 1
#     else:
#         gestures[0][:] = []
#         gestures[1][:] = []
#         drag = 0
#         
# def mouse_released():
#     global drag
#     drag = None
