# shoebot (code to be run with sbot runner)

from math import radians, sin, cos
from math import dist as e_dist
from random import randint
from functools import cache

def setup_points():
    global pts_a, pts_b
    pts_a = create_points()
    pts_b = create_points()


def setup():
    size(600, 600)
    strokewidth(1)
    colorrange(255)
    var('t', NUMBER, 0.0, 0.0, 100.0)
    var('d', NUMBER, 150.0, 50.0, 200.0)
    var("b", BOOLEAN)
    setup_points()

def create_points():
    pontos = []
    for i in range(12):
        r = randint(-10, 10)
        m = 100
        xo = randint(m, WIDTH - m)
        yo = randint(m, HEIGHT - m)
        for a in range(-18, 18):
            x = xo + 5 * r  * a * (-1 if r < 0 else 1)
            y = yo + 5 * r * a  + r * 10 * sin(radians(a * 10))
            pontos.append((int(x), int(y)))
    return tuple(pontos)

def draw():
    global frame_count, b
    background(200)
    stroke(0)
    if b:
        setup_points()
        b = False
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
@cache
def dist(a, b):
    return e_dist(a, b)

@cache
def lerp(a, b, t):
    return a * (1 - t) + b * t

@cache
def lerp_tuple(a, b, t):
    return tuple(
        lerp_tuple(ca, cb, t) if isinstance(ca, tuple) else lerp(ca, cb, t)
        for ca, cb in zip(a, b)
    )
