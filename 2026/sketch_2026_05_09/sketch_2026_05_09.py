# A = n * r * r * sin(TWO_PI / n) / 2
# r = sqrt(2 * A / (n * sin(TWO_PI / n)))

from shapely import Polygon

def setup():
    size(800, 400)
    background(127, 200, 127)
    fill(0)
    no_stroke()
    A = 9000
    x, y = 100, 200;
    for n in range(3, 7):
        r = sqrt(2 * A / (n * sin(TWO_PI / n)))
        with begin_closed_shape():
            vertices(pts := poly(x, y, r, n))
        x += 200
        p = Polygon(pts)
        print(p.area)
    save('out.png')

def poly(x, y, r, n=6, rot=0, rnd=0):
    vs = []
    for i in range(n):
        ox, oy = random(-rnd, rnd), random(-rnd, rnd)
        sx = x + cos(i * TWO_PI / n + rot) * r + ox
        sy = y + sin(i * TWO_PI / n + rot) * r + oy
        vs.append((sx, sy))
    return vs