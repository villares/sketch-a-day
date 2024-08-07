from itertools import product

import py5

def setup():
    py5.size(600, 600)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()

def draw():
    py5.background(100)
    for i, j in product(range(5), repeat=2):
        s = 100
        h = py5.sqrt(3) * s
        v = s * 1.5
        x = i * h + (h / 4 if j % 2 else -h / 4)
        y = j * v
        py5.stroke(255)
        poly(x, y, s, n=6)
    
def poly(x, y, r, n=8, rot=py5.radians(30)):
    poly_pts = []
    for i in range(n):
        sx = x + py5.cos(i * py5.TWO_PI / n + rot) * r
        sy = y + py5.sin(i * py5.TWO_PI / n + rot) * r
        poly_pts.append((sx, sy))
    for a, b, c in triangulate(poly_pts, (x, y)):
        xa, ya = a
        xb, yb = b
        xc, yc = c
        mab = (xa + xb) / 2, (ya + yb) / 2
        mbc = (xc + xb) / 2, (yc + yb) / 2
        xct, yct = line_intersect((c, mab), (mbc, a))
        for sa, sb, sc in triangulate((a, b, c), (xct, yct)):
            py5.triangle(*sa, *sb, *sc)
            
        
def triangulate(pts, center):
    xc, yc = center
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles

    
def line_intersect(*args, **kwargs):
    """
    Adapted from Bernardo Fontes https://github.com/berinhard/sketches/
    """
    as_Py5Vector = kwargs.get('as_Py5Vector', False)
    in_segment = kwargs.get('in_segment', True)
    
    if len(args) == 2:  # expecting 2 Line objects or 2 tuples of 2 point tuples.
        (x1, y1), (x2, y2) = args[0]
        (x3, y3), (x4, y4) = args[1]
    elif len(args) == 4:
        (x1, y1), (x2, y2) = args[:2]
        (x3, y3), (x4, y4) = args[2:]
    elif len(args) == 8:
        x1, y1, x2, y2, x3, y3, x4, y4 = args
    else:
        raise ValueError("line_intersect requires 2 lines, 4 points or 8 coords.")
            
    divisor = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if divisor:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / divisor
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / divisor
    else:
        return None
    if not in_segment or 0 <= uA <= 1 and 0 <= uB <= 1:
        x = x1 + uA * (x2 - x1)
        y = y1 + uA * (y2 - y1)
        return Py5Vector(x, y) if as_Py5Vector else (x, y)
    else:
        return None
    
        
def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)
