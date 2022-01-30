shapes = [( (-300, 300), (-300, -300), (300, -300), (300, 300))]

def setup():
    global img, f
    size(900, 900, P3D)
    noStroke()
    colorMode(HSB)
    for _ in range(5):
        split_shapes()
                
def draw():
    background(240)
    translate(width / 2, height / 2, -1800)
    rotateX(radians(30))
    w = 900
    for i in range(-2, 3):
        for j in range(-3, 2):
            push()
            translate(i * w, j * w)
            module()
            pop()
    
    
def module():
    for s in shapes:
        xc, yc = centroid(s)
        d = 0.5  
        a = poly_area(s)
        fill(a % 255, 100, 200)
        beginShape()
        for x, y in s:
            vertex(x + xc * d, y + yc * d)
        endShape(CLOSE)
        
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
