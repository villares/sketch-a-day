from time import time

shapes = [( (-300, 300), (-300, -300), (300, -300), (300, 300))]

def setup():
    global img, f, t
    size(900, 900, P3D)
    # noStroke()
    strokeWeight(0.5)
    stroke(100)
    fill(0)
    f = createFont('Tomorrow Bold', 100)
    img = createGraphics(width, height)
    for _ in range(9):
        split_shapes()
                
def draw():
    background(240)
    translate(width / 2, height / 2, 0)
    scale(1.5)
    for i, s in enumerate(shapes):
        xc, yc = centroid(s)
        fill(0)
        push() 
        # translate(0, 0, z)
        beginShape()
        d = 1
        for x, y in s:
            vertex(x + xc * d, y + yc * d)
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
        (ab, ca, a),
        (ab, bc, b),
        ( bc, c, ca, ab,)
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
   
   
