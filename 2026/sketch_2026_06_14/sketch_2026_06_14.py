# A = n * r * r * sin(TWO_PI / n) / 2
# r = sqrt(2 * A / (n * sin(TWO_PI / n)))

import py5
from shapely import Polygon
from py5 import sqrt, radians, sin, cos, TWO_PI, random

polys = []

def setup():
    py5.size(800, 400)
    py5.background(127, 200, 127)
    py5.fill(0)
    py5.no_stroke()
    A = 9000
    x = 110
    for n in [3, 4, 5, 6, 24]:
        r = sqrt(2 * A / (n * sin(TWO_PI / n)))        
        y = 200
        if n == 3:
            rot = radians(-90)
            y = 210
        elif n == 4:
            rot = radians(45)
            y = 204
        elif n == 5:
            rot = radians(180 + 18)
            #y = 206
        else:
            rot = 0
        pts = poly(0, 0, r, n, rot=rot)
        p = Polygon(pts)
        py5.shape(p, x, y)
        polys.append(p)
        x += 145
        #print(p.area)
    py5.save('out.png')

def poly(x, y, r, n=6, rot=0, rnd=0):
    vs = []
    for i in range(n):
        ox, oy = random(-rnd, rnd), random(-rnd, rnd)
        sx = x + cos(i * TWO_PI / n + rot) * r + ox
        sy = y + sin(i * TWO_PI / n + rot) * r + oy
        vs.append((sx, sy))
    return vs

py5.run_sketch(block=False)