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
    for _ in range(9 + int(year() - 2022)):
        split_shapes()
    t = int(time() - 1642901850) / 31104000.0
    print(t)
                
def draw():
    img.beginDraw()
    img.clear()
    img.smooth()
    img.textFont(f)
    img.textSize(100)
    img.textLeading(100)
    img.textAlign(CENTER, CENTER)
    txt = '{} {}\n{}\n{} {}\n{:.2f}'.format(day(), month(), year(),
                                     hour(), minute(), 
                                     # t / 31104000.0/
                                     second()
                                     )
    img.text(txt, width / 2, height * 0.485)
    img.endDraw()
    
    background(0)
    translate(width / 2, height / 2, 0)
    scale(1.5)
    for i, s in enumerate(shapes):
        xc, yc = centroid(s)
        c = img.get(xc + width / 2,
                    yc + height / 2)
        if c != 0:
            fill(0)
        else:
            if i > millis() % len(shapes):
                fill(200)
            else:
                fill(0, 100, 200)
            
        push() 
        # translate(0, 0, z)
        beginShape()
        d = (1 - t) / 2.0
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
   
   
