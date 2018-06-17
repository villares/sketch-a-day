# Alexandre B A Villares - https://abav.lugaralgum.com / sketch - a - day
SKETCH_NAME = "s168"  # 180616

add_library('peasycam')

points, lines, walls = [], [], []

def setup():
    global space
    size(600, 600, P3D)
    hint(DISABLE_DEPTH_TEST)
    strokeWeight(2)
    # noSmooth()
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(1000)
    grid_dim = 10
    space = width / grid_dim
    for ix in range(grid_dim):
        for iy in range(grid_dim):
            for iz in range(grid_dim):
                x = space / 2 + ix * space - width / 2 + random(2)
                y = space / 2 + iy * space - width / 2 + random(2)
                z = space / 2 + iz * space - width / 2  # + random(-2, 2)
                points.append(PVector(x, y, z))
    for p in points:
        for op in points:
            if p != op:
                stroke(200, 0, 100)
                if (dist(p.x, p.y, p.z,
                         op.x, op.y, op.z) < space * 1):
                    lines.append((p, op))
    for (p1, p2) in lines:
        for (p3, p4) in lines:
            if p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4:
                if p1.z == p2.z and p3.z == p4.z and p1.z != p3.z:
                    if (dist(p1.x, p1.y, p1.z, p3.x, p3.y, p3.z) < space + 3 and
                            dist(p2.x, p2.y, p2.z, p4.x, p4.y, p4.z) < space + 3):

                        walls.append((p1, p2, p3, p4))

    println(len(walls))


def draw():
    background(200)

    for w in walls:
        p1, p2, p3, p4 = w
        fill(100, 0, 200, 10)
        noStroke()
        beginShape()
        vertex(p1.x, p1.y, p1.z)
        vertex(p2.x, p2.y, p2.z)
        vertex(p4.x, p4.y, p4.z)
        vertex(p3.x, p3.y, p3.z)
        endShape(CLOSE)

    for (p, op) in lines:
        stroke(200, 0, 100)
        line(p.x, p.y, p.z, op.x, op.y, op.z)

    for p in points:
        pushMatrix()
        translate(p.x, p.y, p.z)
        fill(0)
        noStroke()
        box(2)
        popMatrix()
