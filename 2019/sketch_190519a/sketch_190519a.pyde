from itertools import product, combinations, permutations, combinations_with_replacement

space = 30

def setup():
    global line_combos, W, H, position
    size(600, 600)
    frameRate(5)
    rectMode(CENTER)
    strokeWeight(2)
    grid = list(product(range(-1, 2), repeat=2))
    lines = list(combinations(grid, 2))
    short_lines = []
    for l in lines:
        (x0, y0), (x1, y1) = l[0], l[1]
        if dist(x0, y0, x1, y1) <= sqrt(2):
            short_lines.append(l)
    print(len(short_lines))
    line_combos = list(combinations(short_lines, 4))
    print len(line_combos)
    W, H = (width - space) / space, (height - space) / space
    position = 0
    print(W, H)


def draw():
    global position
    colorMode(RGB)
    background(0)
    i = position
    for y in range(H):
        for x in range(W):
            if i < len(line_combos):
                pushMatrix()
                translate(space + space * x, space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1
    if i < len(line_combos):
        position += W

def draw_combo(i):
    colorMode(RGB)
    siz = space / 4
    for i, sl in enumerate(line_combos[i]):
        colorMode(HSB)
        stroke(i * 32, 200, 200)
        (x0, y0), (x1, y1) = sl[0], sl[1]
        line(x0 * siz, y0 * siz, x1 * siz, y1 * siz)
