from collections import deque

positions = deque([Py5Vector()], maxlen = 256)

STEP = 50

def setup():
    size(1024, 768, P3D)
    color_mode(HSB)
    #no_stroke()
    frame_rate(24)
    
def draw():
    background(0)
    f = frame_count / 50.0
    translate(width / 2, height / 2)
    rotate_x(f)
    rotate_z(f / 10.0)
    for i, pos in enumerate(positions):
        fill((i + f * 50) % 256, 200, 200)
        with push_matrix():
            translate(*pos)
            box(STEP - 10)
        pos -= positions[-1] / 10  # moves everyone to center head
    n = int(noise(f) * 20) % 3
    d = int(noise(f) * 20) % 2
    a = (-STEP, STEP)[d]
    movex = a if n==2 else 0
    movey = a if n==1 else 0
    movez = a if n==0 else 0 
    positions.append(positions[-1] + Py5Vector(movex, movey, movez))
