# inspired by https://twitter.com/takawo/status/1164723663200870401

# add_library('peasycam')
from random import randint as ri
from random import seed
from arcs import *

a = 516
s = 1

def setup():
    size(a, a)
    colorMode(HSB)
    strokeWeight(1.5)
    # cam = PeasyCam(this, 500)

def draw():
    background(0)
    # translate(-width/ 2, -height / 2)
    randomSeed(s)
    seed(s)
    t(a // 10, a // 10, a - a // 10 * 2)

def t(x, y, w):
    s = w // ri(2, 3)
    noFill()
    stroke(s * 5, 255, 255)
    for i in range(x, x + w - 1, s):
        for j in range(y, y + w - 1, s):
            if random(1) < .85 and w > 90:
                # translate(0, 0, i  / 32 - j / 32)
                t(i, j, s)
            elif random(1) < .5:
                l(i, j, i + s, j + s, s // 2)
            else:
                l(i, j + s, i + s, j, s // 2)

def l(x1, y1, x2, y2, s):
    var_bar(x1, y1, x2, y2, s/2, s/4)
    # rectMode(CENTER)
    # circle(x1, y1, s)
    # circle(x2, y2, s)
    # rectMode(CORNER)


def keyPressed():
    global s
    if key == ' ':
        redraw()
        s += 1
    if key == 's': saveFrame("#####.png")

    
def var_bar(p1x, p1y, p2x, p2y, r1, r2=None):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    """
    if r2 is None:
        r2 = r1
    #line(p1x, p1y, p2x, p2y)
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        rid = (r1 - r2) / d
        if rid > 1:
            rid = 1
        if rid < -1:
            rid = -1
        beta = asin(rid) + HALF_PI
        with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)
            rotate(angle + HALF_PI)
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            #print((d, beta, ri, x1, y1, x2, y2))
            beginShape()  
            b_arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI, mode=2)
            b_arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta, mode=2)
            endShape(CLOSE)
                
def settings():
    """ print markdown to add at the sketc-a-day page"""
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
