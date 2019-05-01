# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# triternary combinations

from __future__ import division
from arcs import var_bar

order = 5  # for a grid with 25 positions
alt = False

def setup():
    size(720, 720)
    noFill()  # fill(0)
    textAlign(CENTER, CENTER)
    strokeWeight(2)
    smooth(4)
    colorMode(RGB)
    #blendMode(MULTIPLY)

def draw():
    background(200)
    margin = 100
    siz = (width - margin) / order
    if alt:
        grid(siz, margin, draw_tritB)
    else:
        grid(siz, margin, draw_tritA)

def grid(siz, margin, func):
    i = 1
    for x in range(order):
        for y in range(order):
            with pushMatrix():
                translate(margin / 2 + siz / 2 + x * siz,
                          margin / 2 + siz / 2 + y * siz)
                #text(trit(i, pad=4), 0, 0)
                func(trit(i))
            i += 1

def draw_tritA(trits):
    noStroke()
    fill(int(trits[0]) * 128,
         int(trits[1]) * 128,
         int(trits[2]) * 128
         )
    ellipse(0, 0, 64, 64)
    fill(0)
    text(trits, 0, 0)


def draw_tritB(trits):
    # siz = 8
    # pos = [(-siz, -siz),
    #        (+siz, -siz),
    #        (0, +siz/3*2),(0,0)]
    # noFill()
    # for i, qd in enumerate(trits):
    #     q = int(qd)
    #     stroke(63 + i * 64, 255, 128)
    #     var_bar(pos[i][0], pos[i][1],
    #             pos[q][0], pos[q][1],
    #             7, 0)
    pass

def to_base(num, base):
    # inverse of int(str, base)
    BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num:
        result += BS[num % base]
        num //= base
    return result[::-1] or "0"

def trit(n, pad=3):
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
