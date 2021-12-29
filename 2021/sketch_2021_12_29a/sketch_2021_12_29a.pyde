

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    noFill()
    colorMode(HSB)
 
def draw():
    background(0)
    translate(width / 2, height / 2)
    f = radians(frameCount)
    rotateX(f)
    rotateY(QUARTER_PI)
    for db in range(-90, 91, 5):
        b = radians(db)
        R = 210 - db
        beginShape()
        for da in range(360 * 2):
            a = radians(da * 0.5)
            x = R * sin(a) * cos(b)
            y = R * sin(a) * sin(b)
            z = R * cos(a)
            stroke(da / 360.0 * 128,
                abs(db * 2.5),
                255)
            vertex(x, y, z)
        endShape(CLOSE)
    
