
add_library('peasycam')

def setup():
    size(500, 500, P3D)
    cam = PeasyCam(this, 800)
    strokeWeight(3)
        
def draw():
    background(200, 220, 240)
    for x in range(-250, 260, 50):
        for y in range(-250, 260, 50):
            z = 400 - dist(x, y, 0, 0)
            line(x, y, 0, x, y, -z)
