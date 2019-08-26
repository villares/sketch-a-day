
# inspired by https://twitter.com/takawo/status/1164723663200870401

from random import randint as ri

a = 516
def setup():
    size(a, a)
    colorMode(HSB)
    noLoop()

def draw():
    background(0)
    t(a // 10, a // 10, a - a // 10 * 2)

def t(x, y, w):
    s = w // ri(2, 3)
    fill(255, 64)
    stroke(s * 2, 255, 255)
    square(x, y, s)
    # print s
    for i in range(x, x + w - 1, s):
        for j in range(y, y + w - 1, s):
            if random(1) < .9 and w > 90:
                t(i, j, s)
            elif random(1) < .5:
                l(i, j, i + s, j + s, s // 8)
            else:
                l(i, j + s, i + s, j, s // 8)

def l(x1, y1, x2, y2, s):
    line(x1, y1, x2, y2)
    rectMode(CENTER)
    square(x1, y1, s)
    square(x2, y2, s)
    rectMode(CORNER)


def keyPressed():
    if key == ' ': redraw()
    if key == 's': saveFrame("#####.png")
    
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
