def setup():
    size(600, 600, P3D)
    strokeWeight(3)
    noFill()
    colorMode(HSB)

def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(radians(mouseX))
    rotateX(radians(mouseY))
    num_points = 180
    step = TWO_PI / num_points
    for z in range(-width / 2, width / 2, 10):
        beginShape()
        for i in range(num_points):
            sin_a = sin(i * step)
            cos_a = cos(i * step)
            nz = (frameCount + z) * .005
            nx = (100 + 10 * sin_a) * .1
            ny = (100 + 10 * cos_a) * .1
            n = noise(nx, ny, nz)
            r = height / 2 * n
            x = r * sin_a
            y = r * cos_a
            stroke(r % 256, 255, 255)
            vertex(x, y, z)
        endShape(CLOSE)


def keyPressed():
    if key == 's':
        saveFrame("####.png")
