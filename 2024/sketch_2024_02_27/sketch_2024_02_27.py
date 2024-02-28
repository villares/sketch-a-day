from functools import lru_cache

from shapely import Polygon, Point
import py5

def setup():
    py5.size(600,400)
    
def draw():
    global c0, c1
    py5.background(200)
    c0 = make_circle(200, 200, 200).exterior.buffer(30)
    c1 = make_circle(py5.mouse_x, py5.mouse_y, 50)
    s0 = make_star(400, 200, 200, 200).exterior.buffer(30)
    
    if c0.intersects(c1):
        py5.stroke(255, 0, 0)
    else:
        py5.stroke(0)
    py5.fill(255, 128)
    draw_obj(c0)
    
    if s0.intersects(c1):
        py5.stroke(255, 0, 0)
    else:
        py5.stroke(0)
    py5.fill(255, 128)
    draw_obj(s0)
    
    if c0.contains(c1) or s0.contains(c1):
        py5.fill(255, 0, 0, 128)
    else:
        py5.fill(255, 128)
    draw_obj(c1)

def make_star(x, y, w, h):
    return Polygon((
        (x - w / 2, y - h / 2),
        (x, y - h / 4),
        (x + w / 2, y - h / 2),
        (x + w / 4, y),
        (x + w / 2, y + h / 2),
        (x, y + h / 4),
        (x - w / 2, y + h / 2),
        (x - w / 4, y),
        ))

def make_circle(x, y, d):
    return Point(x, y).buffer(d / 2)

def draw_obj(obj):
    ps = convert_obj(obj)
    ps.disable_style()
    py5.shape(ps, 0, 0)

@lru_cache(maxsize=10)
def convert_obj(obj):
    return py5.convert_shape(obj)

def key_pressed():
    py5.save_frame(__file__[:-3] + '.png')

py5.run_sketch(block=False)

