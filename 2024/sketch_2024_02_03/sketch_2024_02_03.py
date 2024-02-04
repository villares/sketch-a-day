from collections import deque  # a double-ended queue

import py5  # check out https://github.com/py5coding 
from py5 import Py5Vector as PVector

history = deque(maxlen=512)  # mouse dragged positions
play = False

def setup():   # py5 will call this once to set things up
    py5.size(600, 400)
    py5.fill(0)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)

def draw():   # py5 will call this in a loop
    py5.background(51)
    for i, (x, y) in enumerate(history):
        py5.stroke(i / 2, 255, 255, 255)
        py5.circle(x, y, 20) #8 + i / 16)
    if play and len(history) > 2:
        to_move = history.popleft()
        first = history[0]
        delta = to_move - first
        last = history[-1]
        history.append(last + delta)

def mouse_pressed():
    global play
    play = False

def mouse_dragged():  # py5 will call this when you drag the mouse
    history.append(PVector(py5.mouse_x, py5.mouse_y))

def mouse_released():
    global play
    play = True

def key_pressed():   # py5 will call this when a key is pressed
    global play
    if py5.key == ' ':
        play = not play
    elif py5.key == 'c':
        history.clear()

py5.run_sketch()