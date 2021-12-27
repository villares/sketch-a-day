

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    noFill()
 
def draw():
    background(240)
    translate(width / 2, height / 2)
    f = radians(frameCount)
    rotateY(-f * 0.5)
    for i in range(15, 31):
        R = 10 * i
        beginShape()
        for da in range(720):
            a = radians(da * 0.5)
            db = 90 * cos(a * 4 + f)
            b = radians(db)
            x = R * sin(a) * cos(b)
            y = R * sin(a) * sin(b)
            z = R * cos(a)
            stroke(0, 90 + db, 180)
            vertex(x, y, z)
        endShape(CLOSE)
