# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import shapely
from shapely import MultiPolygon, Polygon, LineString, MultiLineString
import numpy as np


def setup():
    global poly_pts, hatch
    py5.size(600, 600)
    py5.stroke_cap(py5.ROUND)
    poly_pts = pontos_estrela(300, 300, 250, 150, 8)
    hatch = py5.convert_shape(generate_hatch(
        poly_pts,
        angle=py5.PI /  4
    ))
    for i, s in enumerate(hatch.get_children()):
        s.set_stroke_weight((1 + i) / 10)
        s.set_stroke(py5.color(i * 4, 0, 0 ))

    py5.background(220, 220, 180)
    py5.shape(hatch)
    py5.stroke_weight(6)
    es = edges(poly_pts)
    for ax, ay, bx, by in es:
            dashed_line(ax, ay, bx, by, d=20)    

def pontos_estrela(x_centro, y_centro, raio_a, raio_b, num_pontas):
    angulo_entre_pontas = 360 / num_pontas
    pts = []
    for i in range(num_pontas):  # 0, 1, 2 ... n-1
        angulo = py5.radians(i * angulo_entre_pontas + 90) 
        meio_passo = py5.radians(angulo_entre_pontas) / 2
        x = x_centro + raio_a * py5.cos(angulo)
        y = y_centro + raio_a * py5.sin(angulo)
        pts.append((x, y))
        x = x_centro + raio_b * py5.cos(angulo + meio_passo)
        y = y_centro + raio_b * py5.sin(angulo + meio_passo)
        pts.append((x, y))
    return np.array(pts)

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
 

def draw_poly(poly, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.shape(py5.convert_cached_shape(poly))

def generate_hatch(poly, angle=0, spacing=10, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    if poly.area == 0:
        return MultiLineString()
    diagonal = py5.dist(*poly.bounds)  # diagonal length
    #print(poly.bounds, diagonal, poly.area)
    num = int(diagonal / spacing)
    V = py5.Py5Vector
    centroid = V(poly.envelope.centroid.x, poly.envelope.centroid.y)
    a = V(-diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    b = V(-diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    c = V(+diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    d = V(+diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    lines = [LineString((V.lerp(a, b, i / num), V.lerp(c, d, i / num)))
             for i in range(num + 1)]
    return MultiLineString(lines).intersection(poly)
 
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


