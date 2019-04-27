from __future__ import division

order = 16 # for a grid with 256 positions
alt = False

def setup():
    size(720, 720)
    noFill()  # fill(0)
    textAlign(CENTER, CENTER)
    strokeWeight(2)
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
    rectMode(CENTER)
    noFill()
    step = 6
    for i, q in enumerate(quats):
        siz = 12 + i * step
        radius = siz / 2 - step
        stroke(63 + i * 64, 255, 128)
        # print 63 + i * 64
        if q == '1':
            rect(0, 0, siz, siz, radius)
        elif q == '2':
            rect(0, 0, siz - step, siz + step, radius)
        elif q == '3':
            rect(0, 0, siz + step, siz - step, radius)
        # else q == '0' and nothing is drawn!

def draw_quatB(quats):
    rectMode(CENTER)
    noFill()
    step = 6
    for i, q in enumerate(quats):
        siz = 12 + i * step
        radius = 0 #siz / 2 - step
        stroke(63 + i * 64, 255, 128)
        # print 63 + i * 64
        if q == '1':
            rect(0, 0, siz, siz, radius)
        elif q == '2':
            rect(0, 0, siz - step, siz + step, radius)
        elif q == '3':
            rect(0, 0, siz + step, siz - step, radius)
        # else q == '0' and nothing is drawn!
        
    # for i, q in enumerate(quats):
    #     siz = 12 + i * step
    #     pushMatrix()
    #     radius = siz/2 - step
    #     stroke(63 + i * 64, 255, 255)
    #     # translate(siz/2,siz/2)
    #     rotate(HALF_PI * int(q))
    #     rect(step, step, siz, siz) #, radius)
    #     siz += step
    #     popMatrix()


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
