import py5
from shapely import Polygon
from villares.shapely_helpers import draw_shapely

drag = None
pts = [
    (100, 100),
    (500, 100),
    (500, 500),
    ]

def setup():
    py5.size(600, 600)

def draw():
    py5.background(200)
    #py5.no_fill()
    star(300, 300, 100, 200, 12)

    star(300, 300, 200, 100, 12, rot=py5.PI / 12)

def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy)) // int(10 + 10/(py5.dist(ax, ay, cx, cy)))
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    pts = []
    for t_num in range(0 if first_point else 1, num_points + 1):
        t = t_num / num_points
        x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
        y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
        pts.append((x, y))
    return pts
           
def star(x, y, radius_a, radius_b, n_points, rot=0):
    step = py5.TWO_PI / n_points
    py5.begin_shape()
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a
        sy = py5.sin(ang) * radius_a
        cx = py5.cos(ang + step / 2.) * radius_b
        cy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            py5.vertex(x + cx, y + cy)
#             py5.stroke(255, 0, 0)
#             py5.point(x + cx, y + cy)
#             py5.point(x + cx, y + cy + 10)
        else:
            py5.vertices(quadratic_points(anchor_x, anchor_y, x + sx, y + sy, x + cx, y + cy))
#             py5.stroke_weight(12)
#             py5.stroke(100, 100)
#             py5.points(quadratic_points(anchor_x, anchor_y, x + sx, y + sy, x + cx, y + cy)) # debug
        anchor_x, anchor_y = x + cx, y + cy
    py5.end_shape()
    
py5.run_sketch()