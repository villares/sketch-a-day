# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import shapely
import numpy as np

poly_pts = np.array([
    (100, 100), (300, 150), (500, 100), (450, 300),
    (500, 500), (300, 450), (100, 500), (150, 300)
])

def setup():
    py5.size(600, 600)
    py5.stroke_cap(py5.ROUND)
    
def draw():
    py5.background(220, 220, 180)
    es = edges(poly_pts)
    py5.stroke_weight(4)
    py5.stroke(100, 0, 0)
    fill_points(poly_pts, 10)
    py5.stroke_weight(5)
    py5.stroke(0, 100, 100)
    fill_points(poly_pts, 20)
    #py5.stroke_weight(3)
    py5.stroke(0)
    for ax, ay, bx, by in es:
            dashed_line(ax, ay, bx, by, d=20)
            
def edges(poly_points):
    poly_points = np.asarray(poly_points)
    rolled = np.roll(poly_points, -1, axis=0)
    return np.column_stack((poly_points, rolled))

def dashed_line(*args, d=20):
    global dashes
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    dashes = edges(coords)[:-1:2]
    py5.lines(dashes)

def dotted_line(*args, d=20):
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    py5.points(coords)

def fill_points(poly_pts, d=10):
    poly_pts = np.asarray(poly_pts)
    poly = shapely.Polygon(poly_pts)
    # shapely.prepare(poly)
    minx, miny, maxx, maxy = poly.bounds
    x = np.arange(minx, maxx + d, d)
    y = np.arange(miny, maxy + d, d)
    xx, yy = np.meshgrid(x, y)
    grid = np.column_stack([xx.ravel(), yy.ravel()])
    # mask = np.array([poly.contains(shapely.Point(pt)) for pt in grid])
    # py5.points(grid[mask])
    pts = shapely.MultiPoint(grid).intersection(poly)
    py5.shape(pts) 
 
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


