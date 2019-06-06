# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from var_bar import var_bar

space, border = 40, 0
position = 0  # initial position


def setup():
    global line_combos, W, H, position, num
    size(820, 460)
    frameRate(1)
    rectMode(CENTER)
    strokeWeight(2)
    grid = product(range(-1, 1), repeat=2)  # 2X2
    # all line combinations on a grid
    lines = permutations(grid, 2)
    # allow only some lines
    possible_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) < 2:  # rule defined here...
            possible_lines.append(l)
    num_possible_lines = len(possible_lines)
    println("Number of possible lines: {}".format(num_possible_lines))
    # main stuff
    line_combos = list(combinations(possible_lines, 3))
    # shuffle(line_combos) # ucomment to shuffle!
    num = len(line_combos)
    println("Number of permutations: {}".format(num))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                pushMatrix()
                # B option
                # translate(border / 2 + space + space * x,
                #           border / 2 + space + space * y)
                translate(border + space + space * x,
                          border + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(line_combos):
        # gif_export(GifMaker, SKETCH_NAME)
        # gif_export(GifMaker, SKETCH_NAME[:-1] + "b") # B option
        position += H * W

def draw_combo(n):
    colorMode(RGB)
    blendMode(MULTIPLY)
    siz = space / 2. # B option
    for i, sl in enumerate(line_combos[n]):
        colorMode(HSB)
        fill(i * 64, 128, 128)
        (x0, y0), (x1, y1) = sl[0], sl[1]
        noStroke()
        var_bar(x0 * siz, y0 * siz, x1 * siz, y1 * siz, siz / 8, siz / 4)

def keyPressed():
    global W, H
    if key == "s":
        saveFrame("####.png")

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
