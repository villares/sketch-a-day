from villares import ubuntu_jogl_fix

# 3D studies with Julio Mariutti
# inspired by: https://seoi.net/peni3d/

points = []
rot_y = 0
meridians = 24

def setup():
    size(500, 500, P3D)
    strokeWeight(2)
    noFill()
    colorMode(HSB)

def draw():
    global tmouseX, tmouseY
    translate(width / 2, height / 2)
    tmouseX, tmouseY = mouseX - width / 2, mouseY - width / 2
    rotateY(rot_y)
    background(0)
    
    pm = int(len(points) / 2)  # indice do ponto medio
    # if pm > 0:
    #     circle(points[pm][0], points[pm][1], 15)
    # for p in points:
    #     circle(p[0], p[1], 5)
    
    paralelos = []
    mx, my = 0, 0  # middle
    for a, b in zip(points[:pm], points[-1:pm - 1:-1]):
        d = dist(a[0], a[1], b[0], b[1])
        mx, my = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
        ang = atan2(b[1] - a[1], b[0] - a[0]) + PI
        circulo = [rotate_p(x, y, ang, mx, my) + (z, )
                   for x, y, z in z_circle(mx, my,
                                           d / 2.0,
                                           num_points=meridians)]
        paralelos.append((d, circulo))

    for d, circulo in paralelos:
        stroke(d % 256, 255, 255)
        beginShape()
        for x, y, z in circulo:
            vertex(x, y, z)
        endShape(CLOSE)
        
    stroke(128)
    for i in range(meridians):
        beginShape()
        for d, circulo in paralelos:
            x, y, z = circulo[i]
            vertex(x, y, z)
        vertex(mx, my, 0)
        endShape()

    stroke(255)    
    beginShape()
    for p in points:
        vertex(p[0], p[1], 0)
    endShape()

def mousePressed():
    points[:] = []
    points.append((tmouseX, tmouseY))

def mouseDragged():
    if dist(tmouseX, tmouseY,
            points[-1][0], points[-1][1]) > 15:
        points.append((tmouseX, tmouseY))


def keyPressed():
    global rot_y
    if keyCode == LEFT:
        rot_y -= radians(5)
    if keyCode == RIGHT:
        rot_y += radians(5)
    if key == ' ':
        rot_y = 0

def z_circle(x, y, radius, num_points=16):
    passo = TWO_PI / num_points
    ang = 0
    pts = []
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = x + cos(ang) * radius
        sz = 0 + sin(ang) * radius
        pts.append((sx, y, sz))
        ang += passo  # aumente o ângulo um passo
    return pts

def rotate_p(xp, yp, angle, x0=0, y0=0):
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)
