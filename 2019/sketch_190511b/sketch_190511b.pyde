# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Quaternary combinations - Processing Python Mode

def setup():
    size(700, 700)
    rectMode(CENTER)
    strokeWeight(1)
    textSize(6)
    textAlign(CENTER, BOTTOM)

def draw():
    background(240)
    margin = 10
    order = 16  # for a grid with 256 positions
    siz = (width - 2 * margin) / order
    translate(margin, margin / 2)
    grid(order, siz, draw_quats)

def grid(order, siz, func):
    i = 0
    for y in range(order):
        for x in range(order):
            pushMatrix()
            translate(siz / 2 + x * siz, siz / 2 + y * siz)
            func(to_base_four(i))
            popMatrix()
            i += 1

def draw_quats(quats):
    noFill()
    step = 4
    for i, q in enumerate(quats[::-1]):
        r_siz = 10 + i * step
        radius = r_siz / 2 - step
        if q == '1':
            stroke(0, 0, 0)
            rect(0, 0, r_siz, r_siz, radius)
        elif q == '2':
            stroke(0)
            rect(0, 0, r_siz - step, r_siz + step, radius)
        elif q == '3':
            stroke(0)
            rect(0, 0, r_siz + step, r_siz - step, radius)
        # else q == '0' and nothing is drawn!
    fill(0, 0, 200)
    text(quats, 0, 25)


def to_base_four(num):
    # convert to base 4 & pad to 4 digits
    base = 4
    BS = "0123"
    result = ""
    while num:
        result += BS[num % base]
        num //= base
    while len(result) < 4:
        result = result + "0"
    return result[::-1]

def keyPressed():
    if key == "s":
        saveFrame(SKETCH_NAME + OUTPUT)

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
