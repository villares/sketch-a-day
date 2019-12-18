def setup():
    size(800, 300, P3D)
    strokeWeight(3)
    noFill()
    colorMode(HSB)

def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(radians(mouseX))
    rotateX(radians(mouseY))
    for z in range(-width / 2, width / 2, 15):
        beginShape()
        for i in range(72):
            sin_a = sin(radians(i * 5))
            cos_a = cos(radians(i * 5))
            fra_z = (frameCount + z) * .003
            r = height / 2 * noise(sin_a + abs(cos_a), abs(sin_a) + cos_a, fra_z)
            x = r * sin_a
            y = r * cos_a
            stroke(r % 256, 255, 255)
            vertex(x, y, z)
        endShape(CLOSE)

def caixa(x, y, z,
          w, h=None, d=None, rotX=0, rotY=0, rotZ=0):
    h = w if h is None else h
    d = w if d is None else d
    pushMatrix()
    translate(x, y, z)
    rotateX(rotX)
    rotateY(rotY)
    rotateZ(rotZ)
    box(w, h, d)
    popMatrix()

def keyPressed():
    if key == 's':
        saveFrame("####.png")
