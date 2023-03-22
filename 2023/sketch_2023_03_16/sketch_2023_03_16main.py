"""
Fiddling on code by Tom Larrow exploring Poisson Disc Sampling
"""

import py5
from PoissonDiscSampling import PoissonDiscSampling


def setup():
    """py5 setup block. This runs once at the start"""
    py5.size(800, 800)
    py5.background(255)


def draw():
    """py5 draw block. This normally runs once for each frame,
    but no_loop() can make it only run once"""
    pds_list = []

    background = 240
    py5.background(background)
    py5.color_mode(py5.HSB)
    palette = [py5.color(i * 32, 200, 100) for i in range(4)]

    xo, yo = 100, 50
    for i, color in enumerate(palette):
        left_x, left_y = xo , yo
        w, h = 150, 700
        right_x, right_y = xo + w, yo + h
        xo += w + 10
        separation_radius = py5.random(1.25, 3) * (12 - (3 * i))
        retries = py5.random_int(15, 30)
        size = 12 - 3 * i
        print("starting", i)
        pds_list.append(PoissonDiscSampling(left_x, left_y, right_x, right_y,
                                            separation_radius, size, color,
                                            retries))

    for pds in pds_list:
        pds.draw_background(background)
        pds.draw()

    py5.save_frame("x_0067_####.png", use_thread=True)

py5.run_sketch()
