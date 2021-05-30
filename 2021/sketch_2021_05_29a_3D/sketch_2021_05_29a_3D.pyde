def setup():
    size(500, 500, P3D)

def draw():
    background(200)
    translate(250, 250)
    rotateY(frameCount / 70.0)
    translate(-250, -250)
    bar(100, 100, 100,
        400, 400, -100)


def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar/edge."""
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    # line(x1, y1, z1, x2, y2, z2)
    n, m = 180, 2
    noFill()
    strokeWeight(5)
    pts = []
    for i in range(n * m):
        v = PVector.lerp(p1, p2, i / float(n * m))
        pushMatrix()
        translate(v.x, v.y, v.z)
        rotateZ(the)
        rotateY(phi)
        rotate(radians(i * (frameCount / 20.0) % 360))
        t =  sin(radians(i / float(m))) ** 3 * 100
        x, y, z = modelX(t, 0, 0), modelY(t, 0, 0), modelZ(t, 0, 0)
        popMatrix()
        pts.append((x, y, z))
        # beginContour()
        point(x, y, z)
        # endContour()
    strokeWeight(1)
    beginShape()
    for x, y, z in pts:
        curveVertex(x, y, z)      
    endShape()
    
