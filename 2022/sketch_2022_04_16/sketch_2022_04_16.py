from itertools import product
from random import sample
from math import atan2
from villares.line_geometry import is_poly_self_intersecting
import py5

def setup():
    global grid, poly, new_poly
    py5.size(600, 600)
    grid = list(product(range(150, py5.width - 100, 100), repeat=2))    
    poly = generate_points()
    new_poly = poly[:]

def generate_points():
    pts = sample(grid, 10)
    while is_poly_self_intersecting(pts):
        pts = sample(grid, 7)
    return pts    

def draw():
    global poly
    py5.background(0)
    poly = lerp_tuple(poly, new_poly, 0.05)
    offsets = [list(poly)]
    for _ in range(10):
        offsets.append(offset(offsets[-1], 15))        
    for i, op in enumerate(reversed(offsets)):
        py5.fill(200 - i * 25, 150, i * 25, 120)
        py5.stroke(0)
        draw_poly(op)
    py5.fill(0)
    for x, y in poly:
        py5.circle(x, y, 5)

def draw_poly(poly):
    with py5.begin_closed_shape():
        py5.vertices(poly)

def key_pressed():
    global new_poly
    new_poly = generate_points()

def offset(poly, r):
    result = []
    triples = zip([poly[-1]] + poly[:-1], poly, poly[1:] + [poly[0]])
    for i, ((xa, ya), (xb, yb), (xc, yc)) in enumerate(triples):
        ang0 = py5.atan2(ya - yb, xa - xb)
        ang1 = py5.atan2(yb - yc, xb - xc)
        ang = (ang0 + ang1) / 2 + py5.HALF_PI
        off_x = r * py5.cos(ang)
        off_y = r * py5.sin(ang)
        
#         cc = ccw((xa, ya), (xb, yb), (xc, yc))
#         oc = ccw((xa, ya), (xb, yb), (xb + off_x, yb + off_y))
#         if not (oc ^ cc):
        if point_inside_poly(xb + off_x, yb + off_y, poly):
           off_x, off_y = -off_x, -off_y
        if r < 0:
            off_x, off_y = -off_x, -off_y
        result.append((xb + off_x, yb + off_y))
    return result

# def ccw(*args):
#     """Returns True if the points are arranged counter-clockwise in the plane"""
#     if len(args) == 1:
#         a, b, c = args[0]
#     else:
#         a, b, c = args
#     return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def point_inside_poly(*args):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    if len(args) == 2:
        (x, y), poly = args
    else:
        x, y, poly = args
    inside = False
    for i, p in enumerate(poly):
        pp = poly[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if not isinstance(ca, (float, int))
                 else py5.lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))

py5.run_sketch()
