# Alexandre B A Villares - https://abav.lugaralgum.com / sketch - a - day
SKETCH_NAME = "s170"  # 180618

add_library('peasycam')

points, lines, walls, floors = [], [], [], []

def setup():
    global space
    size(600, 600, P3D)
    # hint(DISABLE_DEPTH_TEST)
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
                x = space / 2 + ix * space - width / 2 + random(10)
                y = space / 2 + iy * space - width / 2 + random(10)
                z = space / 2 + iz * space - width / 2  # + random(-2, 2)
                points.append(PVector(x, y, z))

    for p1 in points:
        for p2 in points:
            if p1 != p2:
                stroke(200, 0, 100)
                if (dist(p1.x, p1.y, p1.z,
                         p2.x, p2.y, p2.z) < space * 1.1):
                    lines.append((p1, p2))

    for (p1, p2) in lines:
        for (p3, p4) in lines:
            if p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4:
                # walls
                if p1.z == p2.z and p3.z == p4.z and p1.z != p3.z:
                    if (dist(p1.x, p1.y, p1.z,
                             p3.x, p3.y, p3.z) < space + 3 and
                        dist(p2.x, p2.y, p2.z,
                             p4.x, p4.y, p4.z) < space + 3):
                        walls.append((p1, p2, p3, p4))
                # floors
                if p1.z == p2.z and p3.z == p4.z and p1.z == p3.z:
                    if (dist(p1.x, p1.y, p1.z,
                             p3.x, p3.y, p3.z) < space + 3 and
                        dist(p2.x, p2.y, p2.z,
                             p4.x, p4.y, p4.z) < space + 3):
                        floors.append((p1, p2, p3, p4))

    println(len(floors))


def draw():
    background(200)
    noStroke()

    fill(0, 0, 200, 100)
    for (p1, p2, p3, p4) in walls:
        beginShape()
        vertex(p1.x, p1.y, p1.z)
        vertex(p2.x, p2.y, p2.z)
        vertex(p4.x, p4.y, p4.z)
        vertex(p3.x, p3.y, p3.z)
        endShape(CLOSE)

    fill(200, 100, 0)
    for (p1, p2, p3, p4) in floors:
        beginShape()
        vertex(p1.x, p1.y, p1.z)
        vertex(p2.x, p2.y, p2.z)
        vertex(p4.x, p4.y, p4.z)
        vertex(p3.x, p3.y, p3.z)
        endShape(CLOSE)

    for (p1, p2) in lines:
        stroke(200, 0, 100)
        line(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z)

    for p in points:
        pushMatrix()
        translate(p.x, p.y, p.z)
        fill(0)
        noStroke()
        box(2)
        popMatrix()
