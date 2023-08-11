import py5
import numpy as np
from shapely import Polygon

from villares.shapely_helpers import draw_shapely # github.com/villares/villares


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
    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(3)
    with py5.begin_shape():
        py5.vertex(*pts[0])
        py5.bezier_vertex(pts[1][0], pts[1][1],
                          pts[2][0], pts[2][1],
                          pts[3][0], pts[3][1],
                          )
    py5.no_stroke()
    py5.fill(255)
    for x, y in pts: 
        py5.circle(x, y, 15)        
    py5.stroke(200, 0, 0)
    for x, y in bezier_points(pts[0][0], pts[0][1],
                                 pts[1][0], pts[1][1],
                                 pts[2][0], pts[2][1],
                                 pts[3][0], pts[3][1],
):
        py5.line(x, y, py5.width / 2, py5.height / 2)

def bezier_points(ax, ay, bx, by, cx, cy, dx, dy, num_points=None, first_point=False):
    if num_points is None:
        num_points = int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(cx, cy, dx, dy)) // 10
    if num_points <= 2:
        return [(ax, ay), (dx, dy)] if first_point else [(dx, dy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) ** 3 * ax + 3 * (1 - t) ** 2 * t * bx + 3 * (1 - t) * t * t * cx + t ** 3 * dx
    y = (1 - t) ** 3 * ay + 3 * (1 - t) ** 2 * t * by + 3 * (1 - t) * t * t * cy + t ** 3 * dy
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