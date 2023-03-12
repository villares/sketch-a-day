"""
Code for py5 (py5coding.org)
"""

from random import choice, sample
import py5

colors = (
    py5.color(255, 200, 0),
    py5.color(200, 0, 0),
    py5.color(0, 0, 200)
    )

def setup():
    py5.size(600, 600)
    s = 5
    py5.scale(1 / s)
    x = y = 0
    for _ in range(25):
        draw_combo(x, y)
        x += py5.width
        if x >= py5.height * s:
            x = 0
            y += py5.height


def draw_combo(x, y):
    with py5.push_matrix():
        a, b, c = sample(colors, 3)
        ra, rb = sample((75, 150, 300), 2)
        if rb < ra:
            ra, rb = rb, ra
        n = choice((3, 4, 5, 6, 7))
        py5.translate(x, y)
        py5.fill(a)
        py5.rect(0, 0, 600, 600)
        py5.no_stroke()
        py5.fill(b)
        star(py5.width / 2, py5.height / 2, ra, rb, n * choice((1, 2)))
        py5.fill(c)
        star(py5.width / 2, py5.height / 2, rb, ra, n := n * choice((1, 2)),
             py5.PI / n * choice((0, 1)))


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
