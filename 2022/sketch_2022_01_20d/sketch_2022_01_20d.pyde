
shapes = [((-200, -200), (200, -200), (200, 200), (-200, 200))]

def setup():
    size(800, 800, P3D)
    noStroke()
    fill(0)
    for _ in range(9):
        split_shapes()
    
def draw():
    background(240)
    translate(width / 2, height / 2 - 50, 0)
    rotateX(0.5)
    for s in shapes:
        xc, yc = centroid(s)
        z = noise(500 + xc * 0.02 - frameCount * 0.03,
                  1000 + yc * 0.02,
                  frameCount * 0.01
                  ) * 100
        push() 
        translate(0, 0, z)
        beginShape()
        f = sqrt(len(shapes)) / 200.0
        for x, y in s:
            vertex(x + xc * f, y + yc * f)
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
        (ab, bc, c, ca),
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
   
   
