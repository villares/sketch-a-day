"""
Based on a 2018 "gesture recording" idea
"""

import py5

data = []
pdelta = 0

def setup():
    py5.size(600, 600)
    py5.no_fill()
    py5.color_mode(py5.HSB)

def draw():
    py5.background(0)
    for x, y, d in  data:
        py5.stroke((d * d * 5)  % 255, 200, 200)
        py5.circle(x, y, d * d * 2)

def mouse_dragged():
    global pdelta
    delta = py5.dist(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
    d = (delta + pdelta) / 2
    pdelta = delta
    data.append((py5.mouse_x, py5.mouse_y, (5 - py5.sqrt(d))))

py5.run_sketch()