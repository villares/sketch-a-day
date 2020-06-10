

def setup():
    size(500, 500)

def draw():
    t(250, 250)

def t(x, y, s=100):
    pp = poly_points(250, 250, s)
    beginShape()
    for p in pp:
        vertex(*p)
    endShape(CLOSE)

def div_points(a, b, n=10):
    return [(lerp(a[0], b[0], float(i) / n),
             lerp(a[1], b[1], float(i) / n))
            for i in range(1, n)]

def poly_points(x, y, r, n=3):
    a = TWO_PI / n
    points = []
    for i in range(n):
        px = x + r * cos(a * i)
        py = y + r * sin(a * i)
        points.append((px, py))
    return points
