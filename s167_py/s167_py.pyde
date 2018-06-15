# Alexandre B A Villares - https://abav.lugaralgum.com / sketch - a - day
SKETCH_NAME = "s167"  # 180615

add_library('peasycam')

pontos, lines = [], []

def setup():
    global space
    size(600, 600, P3D)
    noStroke()
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
                pontos.append(PVector(x, y, z))
    for p in pontos:
        for other in pontos:
            stroke(200, 0, 100)
            if (dist(p.x, p.y, p.z,
                     other.x, other.y, other.z) < space * 1):
                lines.append((p.x, p.y, p.z, other.x, other.y, other.z))

def draw():
    background(200)
    for p in pontos:
        pushMatrix()
        translate(p.x, p.y, p.z)
        fill(0)
        noStroke()
        box(4)
        popMatrix()
    for l in lines:
            stroke(200, 0, 100)
            px, py, pz, ox, oy, oz = l
            line(px, py, pz, ox, oy, oz)
