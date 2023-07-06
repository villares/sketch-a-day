from itertools import product
from random import choice, sample, seed
import py5
from inputs import InputInterface

colors = (
    py5.color(150, 150, 0),
    py5.color(150,0, 0),
    py5.color(0, 0, 150)
    )
    
def setup():
    global inputs
    #py5.size(1200, 600)
    py5.full_screen()
    inputs = InputInterface()

def draw():
    py5.background(0)
    global a1, a2, a3, a4
    a1 = int(inputs.analog_read(1) / 100)
    a2 = int(inputs.analog_read(2) / 2)
    a3 = int(inputs.analog_read(3))
    a4 = int(inputs.analog_read(4))
    seed(a1)
    w = a2 + 3
    rx = (1 + py5.sin(py5.frame_count / (1 + a3 / 10))) / 2
    ry = (1 + py5.cos(py5.frame_count / (1 + a3 / 10))) / 2
    x = y = 0
    while True:
        colors3 = sample(colors, 3)
        n = choice((3, 4, 5, 6, 7))
        rai, rbi = sample((w / 2, w, w * 2), 2)
        raf, rbf = sample((w / 2, w, w * 2), 2)
        ra = py5.lerp(rai / 5, raf / 5, rx)
        rb = py5.lerp(rbi / 5, rbf / 5, ry)
        draw_combo(x, y, w, n, colors3, ra, rb)
        x += w
        if x >= py5.width:
            x = 0
            y += w
        if y > py5.height:
            break

    inputs.update(display=False)


def draw_combo(x, y, w, n, colors3, ra, rb):
    a, b, c = colors3
    with py5.push_matrix():
        if rb < ra:
            ra, rb = rb, ra
        py5.translate(x, y)
        py5.fill(a)
        py5.rect(0, 0, w, w)
        py5.no_stroke()
        py5.fill(b)
        star(w / 2, w / 2, ra, rb, n * choice((1, 2)))
        py5.fill(c)
        star(w / 2, w / 2, rb, ra, n := n * choice((1, 2)),
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

def key_pressed():
    if py5.key == 'p':
       py5.save_frame(f'{py5.frame_count}.png')
    inputs.key_pressed()
    
def key_released():
    inputs.key_released()


py5.run_sketch(block=False)

