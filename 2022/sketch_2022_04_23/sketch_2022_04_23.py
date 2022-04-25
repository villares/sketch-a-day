# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement

space, border = 15, 30
position = 0  # initial position

def setup():
    global line_combos, W, H, position, num
    size(530, 1000)
    frame_rate(5)
    rect_mode(CENTER)
    stroke_weight(2)
    grid = product(range(-2, 2), repeat=2)  # 4X4
    # all line combinations on a grid
    lines_on_grid = combinations(grid, 2)
    # allow only some lines
    possible_lines = []
    for l in lines_on_grid:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) > 2:  # rule defined here...
            possible_lines.append(l)
    num_possible_lines = len(possible_lines)
    print("Number of possible lines: {}".format(num_possible_lines))
    # main stuff
    line_combos = list(combinations(possible_lines, 2))
    # shuffle(line_combos) # ucomment to shuffle!
    num = len(line_combos)
    print("Number of combinations: {}".format(num))
    W, H = 31, 61
    print("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                push_matrix()
                translate(
                    border + space + space * x, border + space + space * y)
                draw_combo(i)
                pop_matrix()
                i += 1
            else:
                no_loop()
    if i < len(line_combos):
        position += W


def draw_combo(n):
    color_mode(RGB)
    siz = space / 4.0
    for i, sl in enumerate(line_combos[n]):
        # colorMode(HSB)

        (x0, y0), (x1, y1) = sl[0], sl[1]
        if x0 == 0 or x1 == 0:
            stroke(0, 0, 128)
        else:
            stroke(0)
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)


def key_pressed():
    global W, H
    if key == "s":
        save_frame("####.png")
    if key == " ":
        W, H = H, W

