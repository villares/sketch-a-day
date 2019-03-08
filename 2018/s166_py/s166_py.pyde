#  Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s166"  # 180614

add_library('peasycam')

pontos = []

def setup():
    global space
    size(600, 600, P3D)
    colorMode(HSB)
    noStroke()
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)

    grid_dim = 20
    space = width / grid_dim
    for ix in range(grid_dim):
        for iy in range(grid_dim):
            for iz in range(grid_dim):
                x = space / 2 + ix * space - width / 2
                y = space / 2 + iy * space - width / 2
                z = space / 2 + iz * space - width / 2
                pontos.append(PVector(x, y, z))
        

def draw():
    background(0)
    for p in pontos:
        pushMatrix()
        translate(p.x, p.y, p.z)
        noiseScale = 0.005
        n = noise(abs(mouseX + p.x) * noiseScale,
                  (1000 + mouseY + p.y) * noiseScale,
                  (300000 + p.z) * noiseScale)
        fill(256 * n, 255, 255)
        box(space * (1 - n))
        popMatrix()
