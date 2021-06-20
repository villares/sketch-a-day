# from villares import ubuntu_jogl_fix

points = []
rot_x = 0
sides = 12

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

    circles = []
    for p in points:
        op = (-p[0], p[1])
        radius = p[0]
        circle_points = z_circle(0, p[1], radius, num_points=sides)
        circles.append(circle_points)

    # for c in circles:
    #     beginShape()
    #     for p in c:
    #         vertex(*p)
    #     endShape(CLOSE)
        
    # for i in range(sides):
    #     beginShape()
    #     for c in circles:
    #         vertex(*c[i])
    #     endShape()

    stroke(255)
    for i in range(sides):
        for ca, cb in zip(circles[:-1], circles[1:]):
            fill(255, 100)
            beginShape()
            vertex(*ca[i])
            vertex(*ca[i - 1])
            vertex(*cb[i - 1])
            vertex(*cb[i])
            endShape()

    stroke(255, 0, 0)
    noFill()    
    beginShape()
    for p in points:
        vertex(p[0], p[1], 0)
    endShape()

def mousePressed():
    points[:] = []
    points.append((tmouseX, tmouseY))

def mouseDragged():
    if dist(tmouseX, tmouseY,
            points[-1][0], points[-1][1]) > 10:
        points.append((tmouseX, tmouseY))

def z_circle(x, y, radius, num_points=16):
    a = TWO_PI / num_points
    return tuple((x + cos(a * i) * radius, y, sin(a * i) * radius)
                  for i in range(num_points))

def keyPressed():
    global rot_x, sides
    if keyCode == UP:
        rot_x -= radians(5)
    if keyCode == DOWN:
        rot_x += radians(5)
    if keyCode == LEFT and sides > 1:
        sides -= 1
    if keyCode == RIGHT:
        sides += 1
