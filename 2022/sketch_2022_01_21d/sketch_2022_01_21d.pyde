
shapes = [( (-300, 300), (-300, -300), (300, -300), (300, 300))]

def setup():
    global img
    size(1200, 600, P3D)
    noStroke()
    fill(0)
    f = createFont('Tomorrow ExtraBold', 100)
    img = createGraphics(width, height)
    img.beginDraw()
    img.smooth()
    img.textFont(f)
    img.textSize(90)
    img.textLeading(90)
    img.textAlign(CENTER, CENTER)
    img.text('Be kind:\nall else\nis details', width / 2, 20 + height / 2)
    img.endDraw()
                
def draw():
    background(240)
    translate(width / 2, height / 2 - 70, 0)
    # rotateX(0.5)
    for s in shapes:
        xc, yc = centroid(s)
        c = img.get(xc + width / 2,
                    yc + height / 2)
        if c != 0:
            push() 
            # translate(0, 0, z)
            beginShape()
            f = sqrt(len(shapes)) / 300.0
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
   
   
