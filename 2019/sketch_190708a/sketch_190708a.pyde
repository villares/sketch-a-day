# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
""" 
More explorations of inerpolated combinations in grids
- Number of possible bars on a 2x2 grid: 12 
- Number of 2-bar combinations: 66
- Cols: 11 Rows: 6 
- Interpolating 6 intermediary bars (total of 8 bars drawn)
- Overlapping slightly the combinations
"""

from random import shuffle
from itertools import product, combinations, permutations
from var_bar import var_bar

space, border = 80, 80
position = 0  # initial position
radius_a, radius_b = space / 8, space / 16

def setup():
    global bar_combos, W, H, position, num
    size(960, 560)
    frameRate(1)
    rectMode(CENTER)
    grid = product(range(-1, 1), repeat=2)  # 2X2 grid
    # all bar possibilities on a grid (they have a direction)
    bars = permutations(grid, 2)
    # allow only some bars
    possible_bars = []
    for l in bars: # filter not applicable on this sketch
        # (x0, y0), (x1, y1) = l[0], l[1]
        # if dist(x0, y0, x1, y1) < 2:  # rule defined here...
            possible_bars.append(l)
    num_possible_bars = len(possible_bars)
    println("Number of possible bars on a 2x2 grid: {}".format(num_possible_bars))
    # main stuff
    n_bars = 2
    bar_combos = list(combinations(possible_bars, n_bars))
    # shuffle(bar_combos) # ucomment to shuffle!
    num = len(bar_combos)
    println("Number of {}-bar combinations: {}".format(n_bars, num))
    W = (width - border) // space
    H = (height - border) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(bar_combos):
                pushMatrix()
                translate(border + space / 2 + space * x,
                          border + space / 2 + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(bar_combos):
        # gif_export(GifMaker, SKETCH_NAME)
        # gif_export(GifMaker, SKETCH_NAME[:-1] + "b") # B option
        position += H * W

def draw_combo(n):
    noFill()
    stroke(0, 0, 100, 200)
    # noStroke()
    # fill(100, 100)
    siz = space #/ 2. # B option
    first_line = bar_combos[n][0]
    next_line = bar_combos[n][1]    
    jn = 8
    for j in range(8): 
        (x0, y0), (x1, y1) = lerp_poly(first_line, next_line, j / (jn - 1.))
        var_bar(x0 * siz, y0 * siz, x1 * siz, y1 * siz,
                radius_a, radius_b)

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
