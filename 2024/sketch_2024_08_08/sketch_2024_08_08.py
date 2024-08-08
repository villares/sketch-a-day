from itertools import product

import py5

def setup():
    py5.size(600, 600)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()

def draw():
    py5.background(100)
    for i, j in product(range(5), repeat=2):
        s = 200
        h = py5.sqrt(3) * s
        v = s * 1.5
        x = i * h + (h / 4 if j % 2 else -h / 4)
        y = j * v
        py5.stroke(255)
        poly(x, y, s)
    
def poly(x, y, r, n=6, rot=py5.radians(30)):
    poly_pts = []
    for i in range(n):
        sx = x + py5.cos(i * py5.TWO_PI / n + rot) * r
        sy = y + py5.sin(i * py5.TWO_PI / n + rot) * r
        poly_pts.append((sx, sy))
    for a, b, c in triangulate(poly_pts):
        for sa, sb, sc in triangulate((a, b, c)):
            for ssa, ssb, ssc in triangulate((sa, sb, sc)):
                    py5.triangle(*ssa, *ssb, *ssc)

    
            
        
def triangulate(pts):
    xs, ys = tuple(zip(*pts))
    xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles

    
        
def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)
