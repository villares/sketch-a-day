add_library('peasycam')  # é preciso baixar/instalar pelo IDE

message = ("Lorem ipsum dolor sit amet,"
         + "consectetur adipiscing elit.")

def setup():
    size(500, 500, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(200)
    textAlign(CENTER, CENTER)
    textMode(SHAPE)
    fonte = createFont("Tomorrow Light", 12)
    textFont(fonte)

    
def draw():
    background(200)
    bar(0, 0, 10, 20, 10, 40, 3)
    bar(50, 30, -30, 20, 10, 30, 3)
    bar(20, 0, 0, 50, 50, -30, 3),

def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar/edge."""
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    fill(0, 0, 200)
    box(weight, weight, p1.dist(p2))
    rotateY(HALF_PI)
    if screenY(0, 0, 0) - screenY(0, 6, 0) > 0: rotateX(PI)
    if screenX(0, 0, 0) - screenX(6, 0, 0) > 0: rotateY(PI)

    fill(0)
    text(message, 0, 0)
    popMatrix()
