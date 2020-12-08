from villares import ubuntu_jogl_fix

points = []
rot_x = 0
SIDES = 12

def setup():
    size(400, 400, P3D)
    stroke(255)
    noFill()
    smooth(8)
    strokeWeight(1.5)

def draw():
    global tmouseX, tmouseY
    tmouseX, tmouseY = mouseX - width / 2, mouseY - width / 2
    translate(width / 2, height / 2)
    rotateX(rot_x)
    background(0)

    beginShape()
    for p in points:
        vertex(p[0], p[1], 0)
    endShape()

    circles = []
    for p in points:
        op = (-p[0], p[1])
        radius = p[0]
        pts = z_circle(0, p[1], radius, num_points=SIDES)
        circles.append(tuple(pts))
        
    for c in circles:
        beginShape()
        for p in c:
            vertex(*p)
        endShape(CLOSE)
        
    for i in range(SIDES):
        beginShape()
        for c in circles:
            vertex(*c[i])
        endShape()

def mousePressed():
    points[:] = []
    points.append((tmouseX, tmouseY))

def mouseDragged():
    if dist(tmouseX, tmouseY,
            points[-1][0], points[-1][1]) > 10:
        points.append((tmouseX, tmouseY))

def z_circle(x, y, radius, num_points=8):
    passo = TWO_PI / num_points
    ang = 0
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * radius
        sz = sin(ang) * radius
        yield((sx, y, sz))
        ang += passo  # aumente o ângulo um passo

def keyPressed():
    global rot_x
    if keyCode == UP:
        rot_x -= radians(5)
    if keyCode == DOWN:
        rot_x += radians(5)
