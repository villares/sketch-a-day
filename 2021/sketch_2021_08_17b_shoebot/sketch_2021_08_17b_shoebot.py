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


def create_points():
    pontos = []
    for i in range(12):
        r = randint(WIDTH / 10, WIDTH / 4)
        xo = randint(r, WIDTH - r)
        yo = randint(r, HEIGHT - r)
        for a in range(36):
            
            x = xo + r * sin(radians(a * 10))
            y = yo + r * cos(radians(a * 10))
            pontos.append((x, y))
    return pontos

def draw():
    global frame_count
    background(200)
    stroke(0)
    var('t', NUMBER, 0.0, 0.0, 100.0)
    pontos = lerp_tuple(pts_a, pts_b, t / 100.0)

    for xa, ya in pontos:
        for xb, yb in pontos:
            not_same = (xa, ya) != (xb, yb)
            if not_same and 30 < dist((xa, ya), (xb, yb)) < 50:
                stroke(0, 0, 128)
                line(xa, ya, xb, yb)
            if not_same and dist((xa, ya), (xb, yb)) < 30:
                stroke(0, 128, 0)
                line(xa, ya, xb, yb)


#     frame_count += 1


def lerp(a, b, t):
    return a * (1 - t) + b * t


def lerp_tuple(a, b, t):
    return tuple(
        lerp_tuple(ca, cb, t) if isinstance(ca, tuple) else lerp(ca, cb, t)
        for ca, cb in zip(a, b)
    )
