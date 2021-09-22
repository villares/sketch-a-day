# To run this you will need to install shoebot.net
# and use the "bot runner" sbot command

from math import sin, cos, pi
from itertools import product
from random import randint, random

hor = lambda x, y, w, h: (2 + w / 50) + (2 + w / 50) * cos(x / w * 2 * pi)
ver = lambda x, y, w, h: (2 + h / 50) + (2 + h / 50) * cos(y / h * 2 * pi)    
       
def grid(xo, yo, w, n=3):
    reduced_w = w // n
    for i in range(n):
        x = xo + i * reduced_w
        for j in range(n):
            y = yo + j * reduced_w
            r = randint(1, 3)
            if reduced_w > 40 and r == 1:
                grid(x, y, reduced_w)
            elif r == 2:
                stroke(0.9)
                region(x, y, reduced_w, reduced_w, hor)
            else:
                stroke(0)
                region(x, y, reduced_w, reduced_w, ver)

def region(xo, yo, w, h, rule):
    for x, y in product(range(xo, xo + w, 5), range(yo, yo + h, 5)):
        s = rule(x - xo, y - yo, w, h)
        ellipse(x, y, s, s)
            

size(960, 960)
background(0.5)
nofill()
ellipsemode(CENTER)
grid(30, 30, WIDTH - 60)
