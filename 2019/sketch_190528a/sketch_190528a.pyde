# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from gif_exporter import gif_export
add_library('GifAnimation')

space, border = 10, 40
position = 0  # initial position


def setup():
    global line_combos, W, H, position, num
    size(700, 700)
    frameRate(5)
    rectMode(CENTER)
    strokeWeight(2)
    grid = product(range(-2, 2), repeat=2)  # 4X4
    # all line combinations on a grid
    lines = combinations(grid, 2)
    # allow only some lines
    possible_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) > 2:  # rule defined here...
            possible_lines.append(l)
    num_possible_lines = len(possible_lines)
    println("Number of possible lines: {}".format(num_possible_lines))
    # main stuff
    line_combos = list(permutations(possible_lines, 2))
    # shuffle(line_combos) # ucomment to shuffle!
    num = len(line_combos)
    println("Number of permutations: {}".format(num))
    W, H = 61, 62
    println((W, H, W * H))
    println("Cols: {} Lines: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                pushMatrix()
                translate(
                    border + space + space * x, border + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
            else:
                noLoop()
    if i < len(line_combos):
        # gif_export(GifMaker, SKETCH_NAME + "-" +  str(num))
        position += W

def draw_combo(n):
    colorMode(RGB)
    siz = space / 3.
    for i, sl in enumerate(line_combos[n]):
        # colorMode(HSB)
        if i:
            stroke(0, 0, 128)
        else:
            stroke(0)
        (x0, y0), (x1, y1) = sl[0], sl[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)

def keyPressed():
    global W, H
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        W, H = H, W

def settings():
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
