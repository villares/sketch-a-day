# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
from gif_exporter import gif_export
add_library('GifAnimation')

space, border = 16, 20
position = 0  # initial position

def setup():
    global tri_combos, W, H, position, num
    size(1240, 648)
    frameRate(1)
    rectMode(CENTER)
    blendMode(MULTIPLY)
    strokeJoin(ROUND)
    grid = product(range(-1, 2), repeat=2)  # 3X3
    # all line permutations on a grid
    points = list(combinations(grid, 3))
    # allow only some lines
    triangles = []
    for p in points:
        n0 = PVector(*p[0])
        n1 = PVector(*p[1])
        n2 = PVector(*p[2])
        if (n1.x * (n2.y - n0.y) +
                n2.x * (n0.y - n1.y) +
                n0.x * (n1.y - n2.y) != 0):
            triangles.append(p)
    num_possible_triangles = len(triangles)
    println("Number of possible triangles: {}".format(num_possible_triangles))
    # main stuff
    tri_combos = list(combinations(triangles, 2))
    # shuffle(tri_combos) # ucomment to shuffle!
    num = len(tri_combos)
    println("Number of combinatrions: {}".format(num))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(tri_combos):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                # translate(border + space + space * x,
                #           border + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(tri_combos):
        # gif_export(GifMaker, SKETCH_NAME)
        position += H * W
    # else:
    #     gif_export(GifMaker, finish=True)

def draw_combo(n):
    colorMode(RGB)
    siz = space / 2
    for i, sl in enumerate(tri_combos[n]):
        colorMode(HSB)
        fill(i * 128, 128, 128)
        (x0, y0), (x1, y1), (x2, y2) = sl[0], sl[1], sl[2]
        # noStroke()
        poly(((x0 * siz, y0 * siz),
              (x1 * siz, y1 * siz),
              (x2 * siz, y2 * siz)))

def keyPressed():
    global W, H
    if key == "s":
        saveFrame("####.png")


def poly(p_list, closed=True):
    beginShape()
    for p in p_list:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

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
