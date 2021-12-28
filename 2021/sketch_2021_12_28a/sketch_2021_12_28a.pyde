

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    noFill()
    colorMode(HSB)
 
def draw():
    background(0)
    translate(width / 2, height / 2)
    f = radians(frameCount)
    rotateY(QUARTER_PI)
    for i in range(15):
        R = 300 - i * 5
        beginShape()
        for da in range(360 * 2):
            a = radians(da * 0.5)
            db = 90 * cos(a + radians(24 * i) + f)
            b = radians(db)
            x = R * sin(a) * cos(b)
            y = R * sin(a) * sin(b)
            z = R * cos(a)
            stroke(da / 360.0 * 128,
                abs(db * 2.5),
                255)
            vertex(x, y, z)
        endShape(CLOSE)
    
