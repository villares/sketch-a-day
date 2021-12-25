
R = 300

def setup():
    size(800,800,P3D)
    strokeWeight(2)
    hint(ENABLE_STROKE_PERSPECTIVE)
    colorMode(HSB)
    print('FELIZ NATAL e BOM 2022!')
 
def draw():
    background(240)
    translate(width / 2, height / 2)
    f = radians(frameCount)
    rotateY(f * 0.5)
    for da in range(720):
        a = radians(da * 0.5)
        db = 90 * cos(a * 9 + f)
        b = radians(db)
        x = R * sin(a) * cos(b)
        y = R * sin(a) * sin(b)
        z = R * cos(a)
        stroke(90 + db, 255, 200)
        line(x * 0.5, y * 0.5, z * 0.5,
            x, y, z)
        
        
