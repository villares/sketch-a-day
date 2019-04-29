from __future__ import division
from arcs import var_bar

order = 16 # for a grid with 256 positions
alt = False

def setup():
    size(720, 720)
    noFill()  # fill(0)
    textAlign(CENTER, CENTER)
    strokeWeight(2)
    smooth(4)
    colorMode(HSB)
    #blendMode(MULTIPLY)

def draw():
    background(240)
    siz = width / order
    if alt:
        grid(siz, draw_quatB)
    else:
        grid(siz, draw_quatA)

def grid(siz, func):
    i = 0
    for x in range(order):
        for y in range(order):
            with pushMatrix():
                translate(siz / 2 + x * siz,
                          siz / 2 + y * siz)
                #text(quat(i, pad=4), 0, 0)
                func(quat(i))
            i += 1

def draw_quatA(quats):
    a, b, c, d = quats
    siz = 8
    ra = int(a) * siz / 4
    rb = int(b) * siz / 4
    rc = int(c) * siz / 4
    rd = int(d) * siz / 4
    noFill()
    stroke((ra + rb) * 16, 255, 128)
    var_bar(0, -siz, 0, +siz, ra, rb)
    stroke((rc + rd) * 16, 255, 128)
    var_bar(-siz, 0, +siz, 0, rc, rd)


def draw_quatB(quats):
    a, b, c, d = quats
    siz = 8
    ra = int(a) * siz / 4
    rb = int(b) * siz / 4
    rc = int(c) * siz / 4
    rd = int(d) * siz / 4
    noFill()
    stroke(0)
    var_bar(0, -siz, 0, +siz, ra, rb)
    var_bar(-siz, 0, +siz, 0, rc, rd)
        



def to_base(num, base):
    # inverse of int(str, base)
    BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num:
        result += BS[num % base]
        num //= base
    return result[::-1] or "0"

def quat(n, pad=4):
    s = to_base(n, 4)
    while len(s) < pad:
        s = "0" + s
    return s[::-1]


def keyPressed():
    global alt, p

    if key == "s":
        saveFrame("###.png")
    if key == "a":
        alt = not alt


def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
