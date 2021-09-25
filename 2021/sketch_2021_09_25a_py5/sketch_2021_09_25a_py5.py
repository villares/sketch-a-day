import py5
from math import sin, cos, pi, dist
from itertools import product
from random import randint, random

inside = lambda x, y, w, h: randint(0, w) < dist((x, y), (w / 2, h / 2))
outside = lambda x, y, w, h: randint(0, w) > dist((x, y), (w / 2, h / 2))

def setup():
    py5.size(960, 960)
    py5.background(32)
    py5.scale(0.25)
    grid(0, 0, py5.width * 4)
    py5.saveFrame('sketch_2021_09_25a.png')
   
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
                py5.stroke(255)
                region(x, y, qw, qw, inside)
            else:
                py5.stroke(255)
                region(x, y, qw, qw, outside)

def region(xo, yo, w, h, rule, ooutsidelap=0.25):
    o = int(w * ooutsidelap)
    for x, y in product(range(xo - o, xo + w + o), range(yo - o, yo + h + o)):
        if rule(x - xo, y - yo, w, h):
            py5.point(x, y)
            
py5.run_sketch()