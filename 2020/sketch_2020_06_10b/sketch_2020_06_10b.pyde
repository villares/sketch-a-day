def setup():
    size(500, 500)
    noStroke()

def draw():
    background(240)
    noStroke()
    tc = poly_points(250, 250, 100, n=24)
    for i, p in enumerate(tc):
        t(p[0], p[1], 100, 5 * i * radians(210))

def t(x, y, s, rot=0, d=71):
    pp = poly_points(x, y, s, 3, rot + PI)
    e0 = div_points(pp[0], pp[1], d)
    e1 = div_points(pp[1], pp[2], d)[::-1]
    fill(0)
    lines = zip(e0, e1)
    for la, lb in zip(lines[:-1:2], lines[1::2]):
        (x0, y0), (x1, y1) = la
        (x3, y3), (x2, y2) = lb
        quad(x0, y0, x1, y1,
             x2, y2, x3, y3)

def div_points(a, b, d=10):
    return [(lerp(a[0], b[0], float(i) / d),
             lerp(a[1], b[1], float(i) / d))
            for i in range(d + 1)]

def poly_points(x, y, r, n, rot=0):
    a = TWO_PI / n
    points = []
    for i in range(n):
        px = x + r * cos(a * i + rot)
        py = y + r * sin(a * i + rot)
        points.append((px, py))
    return points
