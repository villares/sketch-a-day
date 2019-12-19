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
    for z in range(-width / 2, width / 2, 10):
        beginShape()
        for i in range(72):
            sin_a = sin(radians(i * 5))
            cos_a = cos(radians(i * 5))
            fra_z = (frameCount + z) * .003
            n =  noise(abs(cos_a) + sin_a, abs(sin_a) + cos_a, fra_z)
            r = height / 2 * n
            x = r * sin_a
            y = r * cos_a
            stroke(r % 256, 255, 255)
            vertex(x, y, z)
        endShape(CLOSE)


def keyPressed():
    if key == 's':
        saveFrame("####.png")
