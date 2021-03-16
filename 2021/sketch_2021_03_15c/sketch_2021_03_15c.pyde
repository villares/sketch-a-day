from collections import deque

bs = deque([PVector()], maxlen = 256)

def t(v):
   translate(*v)

def setup():
    size(512, 512, P3D)
    colorMode(HSB)
    
def draw():
    clear()
    f = frameCount / 50.0
    t([256] * 3)
    rotateX(f)
    rotateZ(f / 10.0)
    for i, b in enumerate(bs):
        t(b)
        fill((i + frameCount) % 256, 200, 200)
        box(5)
        t(-1 * b)
        b -= bs[-1] / 10.0
    n = int(noise(f) * 20) % 3
    d = int(noise(f) * 20) % 2
    a = (-6, 6)[d]
    print(a)
    bs.append(bs[-1] + PVector(a*(n==2),a*(n==1),a*(n==0)))
