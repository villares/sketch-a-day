# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Trit grids inspired by Arjan vn der Meij @dutchplotter https://twitter.com/arjanvandermeij 

from __future__ import division

order = 9
p = 4
alt = False


def setup():
    size(700, 700)
    noFill()  # fill(0)
    textAlign(CENTER, CENTER)
    rectMode(CENTER)
    strokeWeight(2)
    colorMode(HSB)

def draw():
    background(240)
    siz = width / order
    if alt:
        grid(siz, draw_tritB)
    else:
        grid(siz, draw_tritA)

def grid(siz, func):
    i = 0
    for x in range(order):
        for y in range(order):
            with pushMatrix():
                translate(siz / 2 + x * siz,
                          siz / 2 + y * siz)
                #text(trit(i, pad=4), 0, 0)
                func(trit(i, pad=p))
            i += 1

def draw_tritA(trit):
    r = 32
    for t in trit:
        if t == '0':
            stroke(0, 255, 128)
            rect(0, 0, r, r)
        elif t == '1':
            stroke(256 / 3 * 2, 255, 128)
            rect(0, 0, r / 2, r * 2)
        else:
            stroke(256 / 3, 255, 128)
            rect(0, 0, r * 2, r / 2)
        r -= 8

def draw_tritB(trit):
    r = 32
    for t in trit:
        stroke(8 + r * 7, 255, 128)
        if t == '0':
            rect(0, 0, r, r)
        elif t == '1':
            rect(0, 0, r / 2, r * 2)
        else:
            rect(0, 0, r * 2, r / 2)
        r -= 8

def to_base(num, base):
    # inverse of int(str, base)
    BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num:
        result += BS[num % base]
        num //= base
    return result[::-1] or "0"

def trit(n, pad):
    s = to_base(n, 3)
    while len(s) < pad:
        s = "0" + s
    return s[::-1]


def keyPressed():
    global alt, p

    if key == "s":
        saveFrame("###.png")

    if key == "a":
        alt = not alt
        
    if key == "p":
        p = (p - 1) % 5


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
