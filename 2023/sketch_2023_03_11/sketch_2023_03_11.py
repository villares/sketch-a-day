"""
Code for py5 (py5coding.org)
"""

from random import choice, sample, shuffle
import py5

colors = [
    py5.color(255),
    py5.color(128),
    py5.color(0)
    ]

def setup():
    py5.size(800, 800)
    s = 10
    py5.scale(1 / s)
    x = y = 0
    while y < py5.height * s:
        ra = 350
        rb = choice((100, 150, 200))
        n = choice((4, 5, 6))
        double_a = choice((True, False))
        double_b = choice((True, False))
        shuffle(colors)
        draw_combo(x, y, n, colors, ra, rb, double_a, double_b)
        x += py5.width
        if x >= py5.width * s:
            x = 0
            y += py5.height
    print(x, y)

def draw_combo(x, y, *args):
    n, colors, ra, rb, double_a, double_b = args
    a, b, c = colors
    if rb < ra:
        ra, rb = rb, ra
    with py5.push_matrix():
        py5.translate(x, y)
        py5.fill(a)
        py5.rect(0, 0, py5.width, py5.height)
        py5.no_stroke()
        py5.fill(b)
        star(py5.width / 2, py5.height / 2, ra, rb, n * (1 + double_a),
             py5.HALF_PI +  py5.PI / (n * (1 + double_a)))
        py5.fill(c)
        star(py5.width / 2, py5.height / 2, rb, ra, n * (1 + double_b),
             py5.HALF_PI)


def star(x, y, radius_a, radius_b, n_points, rot=0):
    step = py5.TWO_PI / n_points
    py5.begin_shape()
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a
        sy = py5.sin(ang) * radius_a
        cx = py5.cos(ang + step / 2.) * radius_b
        cy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            py5.vertex(x + cx, y + cy)
        else:
            py5.quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
    py5.end_shape()


py5.run_sketch()
