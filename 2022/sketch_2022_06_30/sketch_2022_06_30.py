from itertools import product
from villares.helpers import lerp_tuple

drag = None
gestures = ([], [])

def setup():
    size(600, 600)

def draw():
    no_stroke()
    background(200)
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
        with begin_shape():
            vertices(lpts)
        stroke_weight(3)
        stroke(100, 0, 0)
        points(lpts)


def mouse_dragged():
    if drag is not None:
        gestures[drag].append((mouse_x, mouse_y))

def mouse_pressed():
    global drag
    if len(gestures[0]) == 0:
        drag = 0
    elif len(gestures[1]) == 0:
        drag = 1
    else:
        gestures[0][:] = []
        gestures[1][:] = []
        drag = 0
        
def mouse_released():
    global drag
    drag = None
