# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from gif_exporter import gif_export
add_library('GifAnimation')

space = 15
position = 0  # initial position


def setup():
    global line_combos, W, H, position, num
    size(1045, 700)
    frameRate(5)
    rectMode(CENTER)
    strokeWeight(2)
    # grid = product(range(-1, 1), repeat=2) # 2X2
    grid = product(range(-1, 2), repeat=2) # 3X3
    # grid = product(range(-2, 2), repeat=2) # 4X4
    
    # all possible lines
    lines = combinations(grid, 2)
    # colect only short lines
    short_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) > 1: # short as defined here...
            short_lines.append(l)
    num_short_lines = len(short_lines)
    println("Number of possible lines: {}".format(num_short_lines))
    # main stuff
    line_combos = list(combinations(short_lines, 4))
    # shuffle(line_combos) # ucomment to shuffle!
    num = len(line_combos)
    println("Number of combinations: {}".format(num))
    W, H = (width - space) / space, (height - space) / space
    println("Cols: {} Lines: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                pushMatrix()
                translate(space + space * x, space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
            else: exit()
    if i < len(line_combos):
        # gif_export(GifMaker, SKETCH_NAME + "-" +  str(num))
        position += W

def draw_combo(combo_n):
    siz = space / 2.
    for stroke_n, stroke_line in enumerate(line_combos[combo_n]):
        colorMode(HSB)
        stroke(stroke_n * 64, 160, 160)
        (x0, y0), (x1, y1) = stroke_line[0], stroke_line[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)

def keyPressed():
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
