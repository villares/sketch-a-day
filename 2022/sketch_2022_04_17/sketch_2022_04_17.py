from itertools import product
from random import choice
from math import atan2, pi, sin, cos
from villares.line_geometry import is_poly_self_intersecting
import py5

def setup():
    global grid, poly, new_poly
    py5.size(600, 600)
    grid = list(product(range(150, py5.width - 100, 100), repeat=2))    
    poly = generate_points()
    new_poly = poly[:]

def generate_points():
    pts = []
    for _ in range(3):
        (x, y), n = choice(grid), choice((3, 5, 7, 11))
        ra, rb = choice((20, 40, 80)), choice((30, 60, 120))
        pts.extend(star(x, y, ra, rb, n))
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
        
        if point_inside_poly(xb + off_x, yb + off_y, poly):
           off_x, off_y = -off_x, -off_y
        if r < 0:
            off_x, off_y = -off_x, -off_y
        result.append((xb + off_x, yb + off_y))
    return result


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
    d = len(a) - len(b)
    if d < 0:
        a = a + a[abs(d):]
    elif d > 0:
        b = b + b[d:]
    return tuple(lerp_tuple(ca, cb, t) if not isinstance(ca, (float, int))
                 else py5.lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))

def star(x, y, ra, rb, n):
    step = 2 * pi / n
    pts = []
    ang = 0
    while ang < 2 * pi:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * ra
        sy = sin(ang) * ra
        pts.append((x + sx, y + sy))
        sx = cos(ang + step / 2.) * rb
        sy = sin(ang + step / 2.) * rb
        pts.append((x + sx, y + sy))
        ang += step 
    return pts

py5.run_sketch()
