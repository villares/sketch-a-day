# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
# add_library('gifAnimation')

space, border = 30, 30
position = 0  # initial position


def setup():
    global line_combos, W, H, position, num
    size(18 * 30 + 60, 23 * 30 + 60)
    frame_rate(5)
    rect_mode(CENTER)
    stroke_weight(4)
    grid = product(range(-2, 1), repeat=2)  # 4X4
    # all line combinations on a grid
    lines_on_grid = list(combinations(grid, 2))
    print("Number of lines: {}".format(len(lines_on_grid)))
    # main stuff disallow only some comos
    raw_line_combos = sorted(combinations(lines_on_grid, 2))
    line_combos = []
    for la, lb in raw_line_combos:
        if not continous(la, lb) or not parallel(la, lb):
             line_combos.append((la, lb))
    num = len(line_combos)
    print("Number of combinations: {}".format(num))
    W, H = 18, 23
    print("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))

def continous(la, lb):
    sa, ea = la
    sb, eb = lb
    return len(set((sa, ea, sb, eb))) < 4

def parallel(la, lb):
    (x0, y0), (x1, y1) = la
    (x2, y2), (x3, y3) = lb
    return abs(abs(atan2(y0 - y1, x0 - x1)) - abs(atan2(y2 - y3, x2 - x3))) > 0.1


def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                push_matrix()
                translate(
                    border + space / 2 + space * x, border + space / 2 + space * y)
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

        (x0, y0), (x1, y1) = sl
        if dist(x0, y0, x1, y1) > 2:
            stroke(0, 128, 0)
        else:
            stroke(0)
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)


def key_pressed():
    global W, H
    if key == "s":
        save_frame("####.png")

