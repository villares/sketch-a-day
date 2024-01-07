from collections import deque

bs = deque([Py5Vector()], maxlen = 256)

S = 50

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
    for i, b in enumerate(bs):
        fill((i + f * 50) % 256, 200, 200)
        with push_matrix():
            translate(*b)
            box(S - 10)
        b -= bs[-1] / 10
    n = int(noise(f) * 20) % 3
    d = int(noise(f) * 20) % 2
    a = (-S, S)[d]
    bs.append(bs[-1] + Py5Vector(a*(n==2),a*(n==1),a*(n==0)))
