s = 0.003

def setup():
    size(500, 500, P3D)

def draw():
    background(0)
    translate(width / 2, height / 2)

    rotate_x(HALF_PI)
    rotate_z(QUARTER_PI)

    translate(-width / 2, -height / 2, 0)

    t = frame_count
    for x in range(10, 500, 20):
        for y in range(10, 500, 20):
            d = 200 * (1 + noise(x * s, y * s, t * s)) / 2
            my_box(x, y, -200 + d / 2, 10, 10, d)
    
def my_box(x, y, z, *args):
    push()
    translate(x, y, z)
    box(*args)
    pop()
    
    
    