

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
    for da in range(0, 360, 10):
        a = radians(da)
        R = 300 #210 - da
        beginShape()
        for db in range(-90, 90, 5):
            b = radians(db)
            x = R * sin(a) * cos(b)
            y = R * sin(a) * sin(b)
            z = R * cos(a)
            stroke(da / 360.0 * 128,
                abs(db * 2.5),
                255)
            vertex(x, y, z)
        endShape(CLOSE)
    
