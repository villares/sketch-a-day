from __future__ import division

order = 9
alt, center = False, False

def setup():
    size(700, 700)
    noFill()  # fill(0)
    textAlign(CENTER, CENTER)
    strokeWeight(2)
    colorMode(HSB)
    blendMode(MULTIPLY)

def draw():
    background(240)
    siz = width / order
    if alt:
        grid(siz, draw_tritB)
    else:
        grid(siz, draw_tritA)

    if center:
        grid(siz, draw_center)

def draw_center(*args):
    stroke(0)
    rectMode(CENTER)
    rect(0, 0, 8, 8)

def grid(siz, func):
    i = 0
    for x in range(order):
        for y in range(order):
            with pushMatrix():
                translate(siz / 2 + x * siz,
                          siz / 2 + y * siz)
                #text(trit(i, pad=4), 0, 0)
                func(trit(i, pad=4))
            i += 1

def draw_tritA(trit):
    rectMode(CENTER)
    noFill()
    siz = 16
    step = 8
    for t in trit:
        radius = siz / 2 - step
        stroke(8 + siz * 7, 255, 128)
        if t == '0':
            rect(0, 0, siz, siz, radius)
        elif t == '1':
            rect(0, 0, siz - step, siz + step, radius)
        else:
            rect(0, 0, siz + step, siz - step, radius)
        siz += step

def draw_tritB(trit):
    rectMode(CORNER)
    noFill()
    siz = 16
    step = 8
    for t in trit:
        radius = 2  # siz/2 - step
        stroke(8 + siz * 7, 255, 128)
        pushMatrix()
        translate(-siz, -siz)
        if t == '0':
            rect(siz / 2, siz / 2, siz, siz, radius)
        elif t == '1':
            rect(siz / 2, siz / 2, siz - step, siz + step, radius)
        else:
            rect(siz / 2, siz / 2, siz + step, siz - step, radius)
        siz += step
        popMatrix()

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
    return s  # if keyPressed else s[::-1]


def keyPressed():
    global alt, center
    if key == "s":
        saveFrame("###" + SKETCH_NAME + ".png")
    if key == "a":
        alt = not alt
    if key == "c":
        center = not center


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
