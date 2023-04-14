"""
Based on a 2018 "gesture recording" idea
"""

import py5
from collections import deque

data = deque(maxlen=512)
pdelta = 0

def setup():
    py5.size(600, 600)
    py5.no_fill()
    py5.color_mode(py5.HSB)

def draw():
    py5.background(0)
    for i, (x, y, d) in enumerate(data):
        py5.stroke(i % 255, 200, 200)
        py5.circle(x, y, d * 2 + d * py5.sin(py5.radians(py5.frame_count)))

def mouse_dragged():
    global pdelta
    delta = py5.dist(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
    d = (delta + pdelta) / 2
    pdelta = delta
    data.append((py5.mouse_x, py5.mouse_y, d))

py5.run_sketch()