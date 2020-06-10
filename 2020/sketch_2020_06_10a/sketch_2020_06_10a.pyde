def setup():
    size(500, 500)
    noStroke()

def draw():
    tc = poly_points(250, 250, 100, n=6)
    for i, p in enumerate(tc):
        t(p[0], p[1], 100,
          5 * i * radians(60))

def t(x, y, s, rot=0):
    pp = poly_points(x, y, s, ,3, rot + PI)
    fill(255)
    beginShape()
    for p in pp:
        vertex(*p)
    endShape(CLOSE)
    e0 = div_points(pp[0], pp[1])
    e1 = div_points(pp[1], pp[2])[::-1]
    stroke(0)
    fill(0)
    lines = zip(e0, e1)
    for la, lb in zip(lines[:-1:2], lines[1::2]):
        (x0, y0), (x1, y1) = la
        (x3, y3), (x2, y2) = lb
        quad(x0, y0, x1, y1,
             x2, y2, x3, y3)

def poly_points(x, y, r, n, rot=0):
    a = TWO_PI / n 
    points = []
    for i in range(n):
        px = x + r * cos(a * i + rot)
        py = y + r * sin(a * i + rot)
        points.append((px, py))
    return points

def div_points(a, b, n=10):
    return [(lerp(a[0], b[0], float(i) / n),
             lerp(a[1], b[1], float(i) / n))
            for i in range(1, n)]
