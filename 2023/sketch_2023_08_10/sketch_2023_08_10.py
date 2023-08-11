import py5
import numpy as np

drag = None
pts = [
    (100, 100),
    (500, 100),
    (500, 500),
    (100, 500),
    ]


def setup():
    py5.size(600, 600)

def draw():
    global num_points
    py5.background(200)
    py5.no_stroke()
    py5.fill(255)
    for x, y in pts: 
        py5.circle(x, y, 15)        
    py5.stroke(200, 0, 0)
    py5.stroke_weight(2)
    for a, b in zip(quadratic_points(pts[0][0], pts[0][1],
                                 pts[1][0], pts[1][1],
                                 pts[2][0], pts[2][1], 50),
                    quadratic_points(pts[0][0], pts[0][1],
                                 pts[3][0], pts[3][1],
                                 pts[2][0], pts[2][1], 50)
                    ):
        py5.line(a[0], a[1], b[0], b[1])
    for a, b in zip(quadratic_points(pts[1][0], pts[1][1],
                                 pts[2][0], pts[2][1],
                                 pts[3][0], pts[3][1], 50),
                    quadratic_points(pts[1][0], pts[1][1],
                                 pts[0][0], pts[0][1],
                                 pts[3][0], pts[3][1], 50)
                    ):
        py5.line(a[0], a[1], b[0], b[1])

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
    
py5.run_sketch()