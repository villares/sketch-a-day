# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org


import py5
import numpy as np


def setup():
    global w, h
    py5.size(600, 600)
    w, h = py5.width, py5.height
    py5.no_fill()
    py5.stroke_weight(2)

def draw():
    global pts
    py5.background(200, 200, 100)
    pts = []
    y = h / 2
    N = 30
    for i in range(N):
        x = i * w / N 
        if i == 0:
            pts.append((x, y))
        else:
            oy = h / 2 if i % 2 else - h / 2
            pts.extend(quadratic_points(
                anchor_x, anchor_y,
                x + w / N / 2, y + oy,
                x + w / N, y))
        anchor_x, anchor_y = x + w / N, y
    with py5.begin_shape():
        py5.vertices(pts)

def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = 20 #int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(ax, ay, cx, cy)) // 10
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
    y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
    return np.column_stack((x, y))

def key_pressed():
    py5.save_frame('out.png')

 
py5.run_sketch(block=False)

