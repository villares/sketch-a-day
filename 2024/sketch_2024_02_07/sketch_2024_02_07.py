from collections import deque  # a double-ended queue

import py5  # check out https://github.com/py5coding 
from py5 import Py5Vector as PVector

history = [deque(maxlen=512)]  # mouse dragged positions
play = False

def setup():  
    py5.size(600, 400)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)

def draw():   
    py5.background(200)
    for k, gesture in enumerate(history):
        for i, p in enumerate(gesture):
            py5.fill(0, 100)
            j = py5.remap(i, 0, len(gesture), 0, py5.TWO_PI)
            d = py5.cos(j) * 20
            py5.circle(*p, d)
        if play and len(gesture) > 2:
            to_move = gesture.popleft()
            first = gesture[0]
            delta = to_move - first
            last = gesture[-1]
            last.x %= py5.width
            last.y %= py5.height
            gesture.append(last + delta)

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