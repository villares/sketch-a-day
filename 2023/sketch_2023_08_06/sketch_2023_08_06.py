import py5
from shapely import Polygon
import numpy as np

from villares.shapely_helpers import draw_shapely # github.com/villares/villares

def setup():
    py5.size(600, 600)

def draw():
    py5.background(200)
    outer = star_points(300, 300, 100, 250, 12)
    inner = star_points(300, 300, 250, 100, 12, rot=py5.PI / 12)
    # in order to make a polygon with holes using Polygon(outer, holes[inner])
    # you have to be sure of the "winding" clockwise/counter-clockwise,
    # so you might preffer star = Polygon(outer).difference(Polygon(inner))
    star = Polygon(outer, [reversed(inner)])
    py5.stroke(0)
    py5.stroke_weight(1)
    draw_shapely(star)
    py5.stroke(200, 0, 0)
    py5.stroke_weight(2)
    py5.points(outer + inner)


def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(ax, ay, cx, cy)) // 10
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
    y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
    return np.column_stack((x, y))
           
def star_points(x, y, radius_a, radius_b, n_points, rot=0):
    if n_points < 3:
        raise TypeError("Number of points sould be at least 3.")
    pts = []
    step = py5.TWO_PI / n_points
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a
        sy = py5.sin(ang) * radius_a
        cx = py5.cos(ang + step / 2.) * radius_b
        cy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            pts.append((x + cx, y + cy))
        else:
            pts.extend(quadratic_points(anchor_x, anchor_y, x + sx, y + sy, x + cx, y + cy))
        anchor_x, anchor_y = x + cx, y + cy
    return pts
    
py5.run_sketch()