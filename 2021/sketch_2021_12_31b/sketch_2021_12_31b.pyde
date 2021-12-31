from __future__ import division

def setup():
    size(700, 700, P3D)
    strokeWeight(2)
    noFill()
    colorMode(HSB)  # Hue, Saturation, Brightness
    noStroke()

def draw():
    lights()
    background(0)
    translate(width / 2, height / 2)
    f = radians(frameCount) * 2
    rotateX(f * 0.5)
    rotateY(1)
    for da in range(5, 180, 5):
        for db in range(-180, 180, 5):
            beginShape(QUAD)
            for i, j in ((0, 0), (5, 0), (5, 5), (0, 5)):
                a = radians(da + i)
                b = radians(db + j)
                pr = 1.1 - abs(da - 90) / 90  # shrink poles
                w = sin(b * 20 + a * 20) * (1 + sin(f + a)) * pr
                R = 230 + 10 * w  # wobbling radius
                x = R * sin(a) * cos(b)
                y = R * sin(a) * sin(b)
                z = R * cos(a)
                fill(da / 180 * 256,      # Hue
                     255,  # Saturation
                     200,
                     # 255 - abs(db * 1.4)
                     )                 # Brightness
                vertex(x, y, z)
            endShape(CLOSE)
