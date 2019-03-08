# Alexandre B A Villares - https://abav.lugaralgum.com / sketch - a - day
SKETCH_NAME = "s167"  # 180615

add_library('peasycam')

points, lines = [], []

def setup():
    global space
    size(600, 600, P3D)
    strokeWeight(2)
    #noSmooth()
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(1000)
    grid_dim = 10
    space = width / grid_dim
    for ix in range(grid_dim):
        for iy in range(grid_dim):
            for iz in range(grid_dim):
                x = space / 2 + ix * space - width / 2 + random(-2, 2)
                y = space / 2 + iy * space - width / 2 + random(-2, 2)
                z = space / 2 + iz * space - width / 2 + random(-2, 2)
                points.append(PVector(x, y, z))
    for p in points:
        for op in points:
            stroke(200, 0, 100)
            if (dist( p.x,  p.y,  p.z,
                     op.x, op.y, op.z) < space * 1):
                lines.append((p, op))

def draw():
    background(200)
    for p in points:
        pushMatrix()
        translate(p.x, p.y, p.z)
        fill(0)
        noStroke()
        box(4)
        popMatrix()
    for (p1, p2) in lines:
            stroke(200, 0, 100)
            line(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z)
