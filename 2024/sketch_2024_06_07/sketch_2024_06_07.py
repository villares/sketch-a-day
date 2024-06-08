from itertools import product, chain

#from shapely import Polygon
import numpy as np
import py5

grid_points = list(product(range(-350, 351, 25), repeat=2))
n = len(grid_points)
w = np.linspace(5, 25, n)
h = np.linspace(25, 5, n)
angs = np.linspace(0, py5.TAU, n)

def setup():
    py5.size(800, 800, py5.P2D)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    global shp
    shp = py5.create_shape()

#def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    rect_geoms = map(rect_maker, zip((grid_points), w, h, angs))
    rect_geoms90 = map(rect_maker, zip((grid_points), w, h, angs + py5.HALF_PI))
    with shp.begin_shape(py5.QUADS):
        v_list = (list(chain.from_iterable(rect_geoms)) +
                  list(chain.from_iterable(rect_geoms90)))
        shp.vertices(v_list)
    shp.set_fills(py5.color(i % 256, 255, 255) for i, _ in enumerate(v_list))
    py5.shape(shp)
    
def rect_maker(t):
    (ox, oy), w, h, angle = t
    return rect_points(ox, oy, w, h, mode=py5.CENTER, angle=angle)
        
def rect_points(ox, oy, w, h, mode=py5.CENTER, angle=None):
    if mode == py5.CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    points = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    if angle is None:
        return points
    else:
        return [rotate_point((x, y), angle, (ox, oy))
                for x, y in points]

def rotate_point(p, angle, origin=(0,0)):
    from py5 import sin, cos
    xp, yp = p
    x0, y0 = origin       
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)

def key_pressed():
    py5.save('out.png')
    
py5.run_sketch(block=False)