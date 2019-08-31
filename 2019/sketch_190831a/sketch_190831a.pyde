from random import randint as ri
from random import choice

s = 3

def setup():
    size(760, 760)
    colorMode(HSB)
    blendMode(MULTIPLY)
    ellipseMode(CORNERS)
    rectMode(CORNERS)
    textAlign(CENTER, CENTER)

def draw():
    background(240)
    # translate(-width/ 2, -height / 2)
    random_seed(s)
    margin = 30 #width // 32
    grid(margin, margin, width - margin * 2) #, width - margin)

def grid(x, y, w, h=None):
    s = w / choice((2, 3, 4))
    # noStroke()
    # fill(s, 255, 200)
    for i in range(x, x + int(1+ w - s), int(s)):
        for j in range(y, y + int(1+ w - s), int(s)):
            fill(s * 2, 255, 200)
            strokeWeight(s / 4)
            if random(1) < .8 and w > 90:
                # translate(0, 0, i  / 32 - j / 32)
                grid(i, j, s)
            elif random(1) < .5:
                rect(i, j, i + s, j + s, s/2)
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

def random_seed(s):
    from random import seed    
    randomSeed(s)
    seed(s)

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
