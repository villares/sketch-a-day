import py5


from functools import cache
from itertools import product
from random import randint, seed

def setup():
    py5.size(1024, 1024)
    py5.background(32)
    py5.scale(0.5)
    seed(1)
    grid(64, 64, py5.width * 2 - 128)
    py5.save_frame('sketch_2022_04_26.png')

def grid(xo, yo, w):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 64 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                py5.stroke(255, 255, 0)
                py5.points(region(x, y, qw, qw, inside))
            else:
                py5.stroke(100, 100, 255)
                py5.points(region(x, y, qw, qw, outside))


def inside(x, y, w, h):
    return randint(0, w) < d(x, y, w / 2, h / 2)

def outside(x, y, w, h):
    return randint(0, w) > d(x, y, w / 2, h / 2)

@cache
def d(xa, ya, xb, yb):
    return (abs(xa - xb) + abs(ya - yb)) * 0.5

def region(xo, yo, w, h, rule, overlap=0.25):
    o = int(w * overlap)
    return [(x, y) for x, y in product(range(xo - o, xo + w + o, 2),
                                       range(yo - o, yo + h + o, 2))
            if rule(x - xo, y - yo, w, h)]


py5.run_sketch()
