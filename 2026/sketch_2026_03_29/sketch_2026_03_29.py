# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import py5_tools

import shapely
from shapely import Polygon

import numpy as np

def setup():
    global polys
    py5.size(600, 600)
    py5.no_stroke()
    
    outer = Polygon(star_points(300, 300, 100, 250, 10, rot=py5.HALF_PI))
    inner = Polygon(star_points(300, 300, 250, 100, 10, rot=py5.HALF_PI + py5.PI / 10 ))
    polys = outer - inner

    py5_tools.animated_gif('out.gif',
                            frame_numbers=range(1, 37),
                            duration=0.03) 
 
def draw():
    py5.background(0)
    w = py5.width
    h = 26
    gap = 10
    start = py5.frame_count % (h + gap)
    for y in range(-start, py5.height, h + gap):
        pontos = ((0, y), (w, y), (w, y + h), (0, y + h))
        p = shapely.Polygon(pontos).buffer(2)
        pi = polys.intersection(p).buffer(2)
        py5.color_mode(py5.HSB)
        py5.fill(pi.area / 100 % 255, 255, 255)
        py5.shape(pi, 0, 0)


 
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

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


