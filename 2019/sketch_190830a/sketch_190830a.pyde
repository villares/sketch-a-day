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
    blendMode(MULTIPLY)
    ellipseMode(CORNERS)
    rectMode(CORNERS)
    # cam = PeasyCam(this, 500)
    # noLoop()
    textAlign(CENTER, CENTER)

def draw():
    background(240)
    # translate(-width/ 2, -height / 2)
    randomSeed(s)
    seed(s)
    grid(a // 10, a // 10, a - a // 10 * 2)

def grid(x, y, w):
    s = float(w) / int(ri(2, 3))
    # noStroke()
    # fill(s, 255, 200)
    for i in range(x, x + int(w) - 1, int(s)):
        for j in range(y, y + int(w) - 1, int(s)):
            fill(s * 2, 255, 200)

            if random(1) < .85 and w > 90:
                # translate(0, 0, i  / 32 - j / 32)
                grid(i, j, s)
            elif random(1) < .5:
                ellipse(i, j, i + s, j + s)
            else:
                rect(i + s, j, i, j + s)
            debug(i, j, s)

def debug(i, j, s):
    if keyPressed and key == "d":
        fill(0)
        text(str(int(s)), i + s / 2, j + s / 2)

def keyPressed():
    global s
    if key == ' ':
        redraw()
        s += 1
    if key == 's':
        saveFrame("#####.png")


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
