# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Trit grid inspired by Arjan vn der Meij @dutchplotter https://twitter.com/arjanvandermeij 

from __future__ import division

order = 9

def setup():
    size(700, 700)
    noFill()# fill(0)
    textAlign(CENTER, CENTER)
    rectMode(CENTER)
    strokeWeight(2)

def draw():
    s = width / order
    i = 0
    for x in range(order):
        for y in range(order):
            with pushMatrix():
                translate(s / 2 + x * s, s/ 2 + y * s)
                #text(trit(i, pad=4), 0, 0)
                draw_trit(trit(i, pad=4))
            i += 1        

def draw_trit(trit):
    r = 8
    for t in trit:
        if t == '0':
            rect(0, 0, r, r)
        elif t == '1':
            rect(0, 0, r/2, r*2)
        else:
            rect(0, 0, r*2, r/2)
        r += 8
    
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
    return s


def keyPressed():
    saveFrame("###.png")
    
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
