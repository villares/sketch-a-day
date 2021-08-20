# shoebot (code to be run with sbot runner)

from math import *
from random import randint

def setup():
    global pts_a, pts_b
    size(600, 600)
    strokewidth(1)
    colorrange(255)
    pts_a = create_points()
    pts_b = create_points()
    var('t', NUMBER, 50.0, 0.0, 100.0)
    var('d', NUMBER, 150.0, 100.0, 200.0)

def create_points():
    pontos = []
    for i in range(12):
        r = randint(-10, 10)
        xo = randint(r, WIDTH - r)
        yo = randint(r, HEIGHT - r)
        for a in range(36):
            x = xo + r  * a * (-1 if r < 0 else 1)
            y = yo + r  * a
            pontos.append((x, y))
    return pontos

def draw():
    global frame_count
    background(200)
    stroke(0)
  
    pontos = lerp_tuple(pts_a, pts_b, t / 100.0)

    for xa, ya in pontos:
        for xb, yb in pontos:
            not_same = (xa, ya) != (xb, yb)
            if not_same and d / 3 < dist((xa, ya), (xb, yb)) < d / 2:
                stroke(0, 0, 128)
                line(xa, ya, xb, yb)
            if not_same and d / 4 - 25 < dist((xa, ya), (xb, yb)) < d / 3:
                stroke(0, 128, 0)
                line(xa, ya, xb, yb)

def lerp(a, b, t):
    return a * (1 - t) + b * t

def lerp_tuple(a, b, t):
    return tuple(
        lerp_tuple(ca, cb, t) if isinstance(ca, tuple) else lerp(ca, cb, t)
        for ca, cb in zip(a, b)
    )
