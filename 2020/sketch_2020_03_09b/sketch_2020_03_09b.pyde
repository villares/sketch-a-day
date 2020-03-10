
ens = []
template = ((-1, -1), (-1, 1), (1, 1), (1, -1))

def setup():
    size(500, 500)
    noFill()
    strokeJoin(ROUND)
    for _ in range(5):
        ens.append(create_points())
               
def create_points():
    pts = []
    for x, y in template:
        w = random(25, 75)
        pts.append((x * w, y * w))
    return pts

def draw():
    background(240)
    translate(width / 2 - 50, height / 2)
    offsets = ens[0]
    for offset, pts in zip(offsets, ens[1:]):
        pushMatrix()
        translate(*offset)
        for dx in range(10):
            pts_copy = pts[:]
            translate(10, 0)
            fc = 5 * dx + frameCount
            pts_copy[2] = lerpPoint(pts_copy[2],
                                    pts_copy[3],
                                    (1 + cos(fc/20.))/2)
            plot_poly(pts_copy)
        popMatrix()
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
        ens[:] = []
        for _ in range(5):
            ens.append(create_points())
    if key == 's':
        saveFrame("####.png")
