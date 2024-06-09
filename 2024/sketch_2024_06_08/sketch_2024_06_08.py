from itertools import product, chain

from shapely import Polygon
import numpy as np
import py5


def setup():
    py5.size(800, 800, py5.P2D)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    global shp
    shp = py5.create_shape(py5.GROUP)

def draw():
#def predraw_update():
    space = 25 #+ py5.mouse_x // 10
    grid_points = list(product(range(-350, 351, space), repeat=2))
    n = len(grid_points)
    w = np.linspace(5, space, n)
    h = np.linspace(space, 5, n)
    angs = np.linspace(0, py5.TAU, n)
    geoms = map(cross_maker, zip((grid_points), w, h, angs))
    for i in range(shp.get_child_count(), -1, -1):
        shp.remove_child(i)
    for geom in geoms:
        shp.add_child(geom)
#def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.shape(shp)
    
def cross_maker(t):
    (ox, oy), w, h, angle = t
    ra = rect_points(ox, oy, w, h, mode=py5.CENTER, angle=angle)
    rb = rect_points(ox, oy, w, h, mode=py5.CENTER, angle=angle + py5.HALF_PI)
    cross = Polygon(ra).union(Polygon(rb))
    shp = py5.convert_shape(cross)
    shp.set_fills(py5.color((py5.degrees(angle) + i * 5)  % 256, 255, 255)
                  for i in range(shp.get_vertex_count()))
    return shp
        
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