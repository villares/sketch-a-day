s = 0.003

def setup():
    size(500, 500, P3D)

def draw():
    background(0)
    # lights()
    translate(width / 2, height / 2)

    rotateX(HALF_PI)
    rotateZ(QUARTER_PI)

    translate(-width / 2, -height / 2, 0)

    t = frameCount
    for x in range(10, 500, 20):
        for y in range(10, 500, 20):
            d = 200 *  noise(x * s, y * s, t * s)
            my_box(x, y, -200 + d / 2, 10, 10, d)
    
def my_box(x, y, z, *args):
    pushMatrix()
    translate(x, y, z)
    box(*args)
    popMatrix()
    
    
    
