"""
Code for py5 (py5coding.org)
"""

from itertools import product
import py5

def setup():
    py5.size(1024, 1024)
    s = 12
    py5.scale(1 / s)
    
    combos = list(product(
        (3, 4, 5),             # num points
        ((255, 0), (0, 255)),  # colors: b & w or w & b
        (100, 300, 500),       # radius a
        (200, 400),            # radius b
        (True, False),         # double a points
        (True, False),         # duouble b points
    ))
    print(len(combos))
    x = y = 0
    while y < py5.height * s and combos:
        combo = combos.pop()
        draw_combo(x, y, *combo)
        x += py5.width
        if x >= py5.width * s:
            x = 0
            y += py5.height
    py5.save('out.png2')

def draw_combo(x, y, *args):
    n, colors, ra, rb, double_a, double_b = args
    a, b = colors
    if rb < ra:
        ra, rb = rb, ra
    with py5.push_matrix():
        py5.translate(x, y)
        py5.fill(200)
        py5.rect(0, 0, py5.width, py5.height)
        py5.no_stroke()
        py5.fill(a)
        star(py5.width / 2, py5.height / 2, ra, rb, n * (1 + double_a),
             py5.HALF_PI +  py5.PI / (n * (1 + double_a)))
        py5.fill(b)
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
