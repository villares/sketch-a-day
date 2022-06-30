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
    stroke(0)
    stroke_weight(2)
    for i, (x1, y1) in enumerate(gestures[1]):
        j = floor(remap(i, 0, len(gestures[1]),
                           0, len(gestures[0])))
        x0, y0 = gestures[0][j]
        for k in range(10):
            xf, yf = lerp_tuple((x0, y0), (x1, y1), k / 10)
            point(xf, yf)
            
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
