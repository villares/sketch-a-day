from collections import deque  # a double-ended queue

import py5  # check out https://github.com/py5coding 
from py5_tools import animated_gif

history = deque(maxlen=360)  # mouse dragged positions

def setup():   # py5 will call this once to set things up
    py5.size(600, 600, py5.P3D)
    py5.color_mode(py5.HSB)

def draw():   # py5 will call this in a loop
    py5.background(0)
    for i, (x, y, r) in enumerate(history):
        with py5.push_matrix():
            py5.translate(py5.width / 2, py5.height / 2)
            py5.rotate_y(r - py5.radians(py5.frame_count))
            py5.translate(-py5.width / 2, -py5.height / 2)            
            h = py5.remap((i - py5.frame_count) % 360, 0, 360, 0, 255)
            py5.fill(h , 255, 255, 150)
            py5.no_stroke()
            py5.translate(x, y) # (i + py5.frame_count) % 3 - 1)
            py5.rotate_y(-r + py5.radians(py5.frame_count))
            d = py5.remap((i - py5.frame_count) % 360, 0, 360, 16, 32)
            py5.circle(0, 0, d)
    if history:
        history.append(history.popleft())

def mouse_dragged():  # py5 will call this when you drag the mouse
    history.append((py5.mouse_x, py5.mouse_y, py5.radians(py5.frame_count)))
    
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == ' ':
        history.clear()
    elif py5.key == 's':
        f = py5.frame_count
        animated_gif('out3.gif', frame_numbers=range(f + 1, f + 361, 4), duration=0.075) 
        
py5.run_sketch()