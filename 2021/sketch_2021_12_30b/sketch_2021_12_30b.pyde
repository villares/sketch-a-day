from __future__ import division

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    noFill()
    colorMode(HSB)  # Hue, Saturation, Brightness
 
def draw():
    background(0)
    translate(width / 2, height / 2)
    f = radians(frameCount) * 2
    rotateX(f * 0.5)
    rotateY(1)
    for da in range(5, 180, 5):
        a = radians(da)
        beginShape()
        for db in range(-180, 180):
            b = radians(db)
            pr = 1.1 - abs(da - 90) / 90 # shrink poles
            w = sin(b * 20) * (1 + sin(f + a)) * pr
            R = 270 + 15 * w # wobbling radius
            x = R * sin(a) * cos(b)
            y = R * sin(a) * sin(b)
            z = R * cos(a)
            stroke(da / 180 * 256,      # Hue
                   255 - abs(db * 1.4), # Saturation
                   255)                 # Brightness
            vertex(x, y, z)
        endShape(CLOSE)
