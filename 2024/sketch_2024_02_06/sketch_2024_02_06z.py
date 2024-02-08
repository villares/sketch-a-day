from collections import deque  # a double-ended queue

import py5  # check out https://github.com/py5coding 
from py5 import Py5Vector as PVector

history = [deque(maxlen=512)]  # mouse dragged positions
play = False

def setup():  
    global pg
    py5.size(600, 400)
    py5.fill(0)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)
    pg = py5.create_graphics(py5.width, py5.height)

def draw():
    #pg.begin_draw()
    py5.background(51)
    for k, gesture in enumerate(history):
        for i, (x, y) in enumerate(gesture):
#             py5.stroke((k * 50 + i / 2) % 255,
#                        255, 255, 255)
            j = py5.remap(i, 0, len(gesture), 0, py5.PI)
            d = py5.cos(j) * 20
            py5.circle(x, y, d)
            
            
        if play and len(gesture) > 2:
            to_move = gesture.popleft()
            first = gesture[0]
            delta = to_move - first
            last = gesture[-1]
            gesture.append(last + delta)
    #pg.end_draw()
    py5.image(pg, 0, 0)
    ne = sum(map(len, history))   # number of elements
    fr = round(py5.get_frame_rate()) # estimaated frame rate
    py5.window_title(f'fr:{fr} ne:{ne}')
    
def mouse_pressed():
    global play
    play = False

def mouse_dragged():  # py5 will call this when you drag the mouse
    gesture = history[-1]
    gesture.append(PVector(py5.mouse_x, py5.mouse_y))

def mouse_released():
    global play
    history.append(deque(maxlen=512))
    play = True

def key_pressed():   # py5 will call this when a key is pressed
    global play
    if py5.key == ' ':
        play = not play
    elif py5.key == 'c':
        history[:] = [deque(maxlen=512)]

py5.run_sketch()


"""
image = Py5Shape_set_fills_0.png

def setup():
    py5.size(100, 100, py5.P2D)

    py5.no_stroke()

    rect = py5.create_shape()
    with rect.begin_closed_shape():
        rect.vertex(10, 10)
        rect.vertex(10, 90)
        rect.vertex(90, 90)
        rect.vertex(90, 10)

    fills = [py5.color(x * 85, 0, 0) for x in range(4)]
    rect.set_fills(fills)

    py5.shape(rect)
"""