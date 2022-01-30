shapes = [( (-300, 300), (-300, -300), (300, -300), (300, 300))]

def setup():
    global img, f
    size(900, 900, P3D)
    noStroke()
    colorMode(HSB)
    for _ in range(9):
        split_shapes()
                
def draw():
    background(0)
    translate(width / 2, height / 2, -200)
    rotateX(radians(20))
    for s in shapes:
        xc, yc = centroid(s)
        d = 0.5  
        a = poly_area(s)
        fill(a % 255, 200, 200)
        push()
        translate(0, 0, a / 10)
        beginShape()
        curveVertex(s[-1][0] + xc * d, s[-1][1] + yc * d)
        for x, y in s:
            curveVertex(x + xc * d, y + yc * d)
        curveVertex(s[0][0] + xc * d, s[0][1] + yc * d)
        curveVertex(s[1][0] + xc * d, s[1][1] + yc * d)
        endShape(CLOSE)
        pop()
        
def split_quad(q):
    return q[:3], q[2:] + q[:1]

def split_tri(t):
    a, c, b = t
    ab = centroid((a, b))
    bc = centroid((b, c))
    ca = centroid((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
        (c, ca, ab, bc)
        )

def centroid(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))

def keyPressed():
    if key == ' ':
        saveFrame('{}.png'.format(len(shapes)))
        split_shapes()


def split_shapes():
    new_shapes = []
    for s in shapes:
        if len(s) == 4:
            new_shapes.extend(split_quad(s))
        else:
            new_shapes.extend(split_tri(s))
    shapes[:] = new_shapes
   
def poly_area(points):
    points = list(points)
    area = 0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0
