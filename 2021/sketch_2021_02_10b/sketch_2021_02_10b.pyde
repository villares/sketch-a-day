add_library('peasycam')  # é preciso baixar/instalar pelo IDE

m1 = "Lorem" 
m2 = "ipsum dolor "
m3 =  "sit amet, consectetur adipiscing elit."

def setup():
    size(500, 500, P3D)
    cam = PeasyCam(this, 300)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(200)
    textAlign(CENTER)
    textMode(SHAPE)
    fonte = createFont("Tomorrow Bold", 18)
    textFont(fonte)

def draw():
    background(64, 128, 200)
    text_line(m1, 0, 0, 10, 50, 10, 40, 3)
    text_line(m2, 50, 100, -30, 20, 10, 30, 3)
    text_line(m3, -100, 0, 0, 50, 50, -30, 3),

def text_line(txt, x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a text_line/edge."""
    stroke(0, 0, 200)
    line(x1, y1, z1, x2, y2, z2)
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    # box(weight, weight, p1.dist(p2))
    rotateY(HALF_PI)
    if screenY(0, 0, 0) - screenY(0, 6, 0) > 0: rotateX(PI)
    if screenX(0, 0, 0) - screenX(6, 0, 0) > 0: rotateY(PI)
    fill(0)
    text(truncate_text(txt, p1.dist(p2)), 0, 4)
    popMatrix()
    
    
    
def truncate_text(txt, tw):
    w = 0
    p = 0
    while w < tw and p < len(txt):
        p += 1
        w = textWidth(txt[:p])
    return txt[:p] 
        
            
                    
