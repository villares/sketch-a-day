
pts = []

def setup():
    size(500, 500)
    noFill()
    strokeJoin(ROUND)
    create_points()

def create_points():
    pts[:] = []
    for i in range(4):
        pts.append((random(100, width - 100), random(100, height - 100)))

def draw():
    background(240)
    pts_copy = pts[:]
    for dx in range(10):
        translate(10, 0)
        pts_copy[0] = lerpPoint(pts_copy[0], pts_copy[1], 0.1)
        plot_poly(pts_copy)

def lerpPoint(a, b, t):
    c = [lerp(ea, eb, t) for ea, eb in zip(a, b)]
    return c

def plot_poly(points):
    beginShape()
    for p in points:
        vertex(*p)
    endShape(CLOSE)

def keyPressed():
    if key == ' ':
        create_points()
    if key == 's':
        saveFrame("####.png")
