# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More explorations of lines in grids

from random import shuffle
from itertools import product, combinations, permutations, combinations_with_replacement
# add_library('gifAnimation')

space, border = 14, 20
position = 0  # initial position

W, H = 96, 73


def setup():
    global line_combos, W, H, position, num
    size(W * space + 40, H * space + 40)
    frame_rate(5)
    rect_mode(CENTER)
    stroke_weight(2)
    grid = product(range(-2, 2), repeat=2)  # 4X4
    # all line combinations on a grid
    lines_on_grid = list(combinations(grid, 2))
    print("Number of lines: {}".format(len(lines_on_grid)))
    # main stuff disallow only some comos
    raw_line_combos = sorted(combinations(lines_on_grid, 2))
    line_combos = []
    for la, lb in raw_line_combos:
        sa, ea = la
        sb, eb = lb
        pts = set((sa, ea, sb, eb))
        if len(pts) > 3 or triangle_area(*pts) > 0:        
             line_combos.append((la, lb))
    num = len(line_combos)
    print("Number of combinations: {}".format(num))
    print("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))

def triangle_area(a, b, c):
    return abs(a[0] * (b[1] - c[1]) +
               b[0] * (c[1] - a[1]) +
               c[0] * (a[1] - b[1]))

def draw():
    global position
    background(240)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                push_matrix()
                translate(border + space / 2 + space * x,
                          border + space / 2 + space * y)
                draw_combo(i)
                pop_matrix()
                i += 1
            else:
                no_loop()
    if i < len(line_combos):
        position += W


def draw_combo(n):
    color_mode(RGB)
    siz = space / 4
    for i, sl in enumerate(line_combos[n]):
        (x0, y0), (x1, y1) = sl
        if x0 == x1 or y0 == y1:
            stroke(0, 0, 100)
        else:
            stroke(0)
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)
        #translate(3, 3) # for debug

def key_pressed():
    global W, H
    if key == "s":
        save_frame("####.png")

