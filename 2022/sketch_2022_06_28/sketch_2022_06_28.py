# Using py5coding.org on Thonny with thonny-py5mode for imported mode

from itertools import product
import py5_tools

#from villares.helpers import save_png_with_src

W = 30

def setup():
    size(1806, 496)
    stroke_join(ROUND)
    background(200)
    cols, rows = 40, 9
    H = W * sqrt(3) * 0.5  # W * sin(radians(60))
    steps = width / 720    # ~5
    for i, j in product(range(cols), range(rows)):
        x = i * W * 1.5 + W - 2
        if i % 2 == 0:
            y = j * H * 2 + H
        else:
            y = j * H * 2 + H * 2
        a0 = remap(x, 0, width, 0, TWO_PI)
        n = round(4 + 4 * sin(a0)) + 3
        a1 = remap(x, 0, width, 0, TWO_PI) + PI
        a2 = remap(x, 0, width, 0, TWO_PI)
        a3 = remap(x, 0, width, 0, TWO_PI)
        no_stroke()
        fill(100, 200)
        d = H / 2 + H / 2 * cos(a1)
        star(x, y, d, H / 2, n)
        stroke_weight(2)
        no_fill()
        stroke(0)
        d = H / 2 + H / 2 * sin(a2)
        star(x, y, d, H / 2, n)
        d = H / 2 + H / 2 * cos(a3)
        stroke(255)
        star(x, y, d, H / 2, n)

#    save_png_with_src()

def star(cx, cy, ra, rb, n=7, start_ang=0):  # estrela
    step = TWO_PI / n
    begin_shape()
    for i in range(n):  # for each tip/point
        ang = start_ang + step * i  # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)


