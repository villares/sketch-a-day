# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
More explorations of inerpolated combinations in grids
- Number of possible bars on a 2x2 grid: 12 
- Number of 3-bar combinations: 220
- Cols: 20 Rows: 11 
- Interpolating 2 intermediares each bar pair
"""

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from var_bar import var_bar

space, border = 55, 0
position = 0  # initial position


def setup():
    global bar_combos, W, H, position, num
    size(1122, 628)
    frameRate(1)
    rectMode(CENTER)
    strokeWeight(2)
    grid = product(range(-1, 1), repeat=2)  # 2X2
    # all line combinations on a grid
    bars = permutations(grid, 2)
    # allow only some bars
    possible_bars = []
    for l in bars:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) < 2:  # rule defined here...
            possible_bars.append(l)
    num_possible_bars = len(possible_bars)
    println("Number of possible bars on a 2x2 grid: {}".format(num_possible_bars))
    # main stuff
    n_bars = 3
    bar_combos = list(combinations(possible_bars, n_bars))
    # shuffle(bar_combos) # ucomment to shuffle!
    num = len(bar_combos)
    println("Number of {}-bar combinations: {}".format(n_bars, num))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(bar_combos):
                pushMatrix()
                # B option
                # translate(border / 2 + space + space * x,
                #           border / 2 + space + space * y)
                translate(border + space + space * x,
                          border + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(bar_combos):
        # gif_export(GifMaker, SKETCH_NAME)
        # gif_export(GifMaker, SKETCH_NAME[:-1] + "b") # B option
        position += H * W

def draw_combo(n):
    colorMode(HSB)
    blendMode(MULTIPLY)
    noStroke()
    siz = space / 2. # B option
    bar_combo = bar_combos[n]
    combo_len = len(bar_combo)
    for i, single_line in enumerate(bar_combo):
        ni = (i + 1) % combo_len
        next_line = bar_combo[ni]
        for j in range(4): 
            c = lerpColor(color(i * 64, 128, 128), color(ni * 64, 128, 128), j)
            fill(c)
            (x0, y0), (x1, y1) = lerp_poly(single_line, next_line, j / 3.)
            var_bar(x0 * siz, y0 * siz, x1 * siz, y1 * siz, siz / 16, siz / 8)

def keyPressed():
    global W, H
    if key == "s":
        saveFrame("####.png")

def lerp_poly(p0, p1, t):
    pts = []
    for sp0, sp1 in zip(p0, p1):
        pts.append((lerp(sp0[0], sp1[0], t),
                   lerp(sp0[1], sp1[1], t)))
    return pts

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
