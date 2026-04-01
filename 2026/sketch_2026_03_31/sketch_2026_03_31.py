# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import numpy as np

drag = None
pts = [
    (200, 100),
    (100, 100),
    ]

num_points = 12

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)

def draw():
    global num_points
    py5.background(200)
    
    py5.stroke_weight(10) 
    py5.no_fill()
    py5.stroke(0, 0, 200, 100)
    py5.points(star_points(
        300, 300,
        pts[0][0], pts[1][0],
        num_points,
        w_a=pts[0][1]/100, w_b=pts[1][1]/100
        )
    )
    py5.fill(200, 0, 0)
    py5.no_stroke()
    for x, y in pts: 
        py5.circle(x, y, 15)       

def star_points(x, y, radius_a, radius_b, n_points, rot=0, w_a=1, w_b=1):
    if n_points < 3:
        raise TypeError("Number of points sould be at least 3.")
    pts = []
    step = py5.TWO_PI / n_points
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a * w_a
        sy = py5.sin(ang) * radius_a
        vx = py5.cos(ang + step / 2.) * radius_b * w_b
        vy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            pts.append((x + vx, y + vy))
        else:
            pts.extend(quadratic_points(anchor_x, anchor_y, x + sx, y + sy, x + vx, y + vy))
        anchor_x, anchor_y = x + vx, y + vy
    return pts


def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(ax, ay, cx, cy)) // 10
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
    y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
    return np.column_stack((x, y))

def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(pts):
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < 10:
            drag = i
            break

def mouse_dragged():
    if drag is not None:
        pts[drag] = (py5.mouse_x, py5.mouse_y)

def mouse_released():
    global drag
    drag = None
    
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


