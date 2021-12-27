

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    noFill()
 
def draw():
    background(0)
    translate(width / 2, height / 2)
    f = radians(frameCount)
    rotateY(1)
    R = 300
    beginShape()
    for da in range(360 * 12):
        a = radians(da)
        db = 45 * sin(a * 12 + f * 2) \ 
           + 45 * cos(a * 0.05)
        b = radians(db)
        x = R * sin(a) * cos(b)
        y = R * sin(a) * sin(b)
        z = R * cos(a)
        stroke(abs(db * 2.5),
               da / 360.0 * 20,
               255)
        vertex(x, y, z)
    endShape(CLOSE)
    
