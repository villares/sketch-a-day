# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from gif_exporter import gif_export
add_library('GifAnimation')

space = 40
num_lines = 5
position = 0


def setup():
    global line_combos, W, H, position, num
    size(600, 600)
    frameRate(5)
    rectMode(CENTER)
    strokeWeight(1)
    # grid = product(range(-1, 1), repeat=2) # 2X2
    grid = product(range(-1, 2), repeat=2) # 3X3
    # grid = product(range(-2, 2), repeat=2) # 4X4
    lines = combinations(grid, 2)
    short_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) <= sqrt(2):
            short_lines.append(l)
    print(len(short_lines))
    line_combos = list(combinations(short_lines, num_lines))
    shuffle(line_combos)
    num = len(line_combos)
    W, H = (width - space) / space, (height - space) / space
    print(W, H)


def draw():
    global position
    colorMode(RGB)
    background(240)
    fill(0)
    textSize(24)
    text(str(num), space, height - space/4)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                pushMatrix()
                translate(space + space * x, space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(line_combos):
        # gif_export(GifMaker, SKETCH_NAME + "-" +  str(num))
        position += W

def draw_combo(i):
    colorMode(RGB)
    siz = space / 2 - 2
    for i, sl in enumerate(line_combos[i]):
        colorMode(HSB)
        # stroke(i * 32, 200, 200)
        (x0, y0), (x1, y1) = sl[0], sl[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)

def keyPressed():
    if key == "s":
        saveFrame("####.png")
        
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
