from collections import deque  # a double-ended queue
import py5  # check out https://github.com/py5coding 

history = deque(maxlen=512)  # mouse dragged positions

def setup():   # py5 will call this once to set things up
    py5.size(600, 400)
    py5.fill(0)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)

def draw():   # py5 will call this in a loop
    py5.background(51)
    for i, (x, y) in enumerate(history):
        py5.stroke(i / 2, 255, 255, 255)
        py5.square(x, y, 20) #8 + i / 16)
    if history:
        history.append(history.popleft())

def mouse_dragged():  # py5 will call this when you drag the mouse
    history.append((py5.mouse_x, py5.mouse_y))
    
def key_pressed():   # py5 will call this when a key is pressed
    history.clear()

py5.run_sketch()