# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of combinations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
# from gif_exporter import gif_export
# add_library('GifAnimation')

space = 10
position = 0  # initial position
mode = 0

def setup():
    global possible_lines, line_combos, W, H, position, num
    size(1340, 560)
    frameRate(5)
    rectMode(CENTER)
    # grid = product(range(-1, 1), repeat=2) # 2X2
    # grid = product(range(-1, 2), repeat=2) # 3X3
    grid = product(range(-2, 2), repeat=2) # 4X4
    
    # all line cmbinations
    grid_lines = combinations(grid, 2)
    # colect only some lines
    possible_lines = []
    for l in grid_lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) > 3: # with rule defined here...
            possible_lines.append(l)
    num_possible_lines = len(possible_lines)
    println("Number of possible lines: {}".format(num_possible_lines))
    # main stuff
    line_combos = list(combinations(possible_lines, 4))
    num = len(line_combos)
    println("Number of combinations: {}".format(num))
    W, H = (width - space) / space, (height - space) / space
    println("Cols: {} Rows {} Visible grid: {}".format(W, H, W * H))


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
            else: noLoop()
    if i < len(line_combos):
        position += W

def draw_combo(combo_n):
    colorMode(HSB)
    siz0 = space / 3. -0.5
    siz1 = space / 3.
    for stroke_n, stroke_line in enumerate(line_combos[combo_n]):
        if mode < 2:
            stroke(0)
        else:
            stroke(stroke_n * 64, 160, 160)
        if mode > 0:
            siz = siz1
        else:
            siz = siz0
        (x0, y0), (x1, y1) = stroke_line[0], stroke_line[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)


def keyPressed():
    global mode
    if key == "s":
        saveFrame("mode-"+str(mode)+"-##.png")
    # if key == "g":
    #     gif_export(GifMaker, SKETCH_NAME, delay=1200)
    if key == "m":
        mode = (mode + 1) % 3
    if key == "r":
        shuffle(line_combos) # ucomment to shuffle!
    if key == "R":
        line_combos[:] = list(combinations(possible_lines, 4))

                
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
