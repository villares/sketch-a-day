from random import randint, choice
from collections import deque

l = deque([PVector()], maxlen = 40)

def t(v):
   translate(*v)

def setup():
    size(512, 512, P3D)
    # noStroke()
    
def draw():
    clear()
    f = frameCount / 50.0
    t([256] * 3)
    rotateX(f)
    rotateZ(f / 10.0)
    for b in l:
        t(b)
        box(5)
        t(b*-1)
        b.sub(l[-1] / 10.0)
    n=int(noise(f) * 20) % 4
    d=int(noise(f) * 20) % 2
    a=(-6, 6)[d]
    l.append(l[-1] + PVector(a*(n==3),a*(n==2),a*(n==1)))
