from math import sin, cos, pi
from itertools import product
from random import randint, random

hor = lambda x, y, w, h: 5 + 5 * sin (y / pi) < 5 + 5 * cos(x / w * 2 * pi)
ver = lambda x, y, w, h: 5 + 5 * sin (x / pi) < 5 + 5 * cos(y / h * 2 * pi)    


size(960, 960)
    
   
def grid(xo, yo, w):
    qw = w // 4
    for i in range(4):
        x = xo + i * qw
        for j in range(4):
            y = yo + j * qw
            r = randint(1, 3)
            if qw > 40 and r == 1:
                grid(x, y, qw)
            elif r == 2:
                stroke(1, 0, 0)
                region(x, y, qw, qw, hor)
            else:
                stroke(1)
                region(x, y, qw, qw, ver)

def region(xo, yo, w, h, rule):
    for x, y in product(range(xo, xo + w, 5), range(yo, yo + h, 5)):
        if rule(x - xo, y - yo, w, h):
            ellipse(x, y, 5, 5)
            

background(0)
nofill()
ellipsemode(CENTER)
grid(5, 5, WIDTH - 10)
