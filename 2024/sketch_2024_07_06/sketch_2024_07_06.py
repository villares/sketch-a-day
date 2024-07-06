from itertools import product

import py5, py5_tools
import numpy as np

def setup():
    global px, w, h
    py5.size(500, 500)
    w, h = py5.width, py5.height
    py5.background(0)
    py5.fill(255)
    py5.no_stroke()
    for x, y in product(range(50, 500, 50), repeat=2):
        py5.circle(x, y, 45)
    px = py5.get_np_pixels(bands='RGB')
    py5_tools.animated_gif('out.gif', count=150, period=0.2, duration=0.2)

    
def draw():
    s = 100
    f = py5.frame_count // s
    py5.random_seed(f)

    direction = py5.random_choice((-1, 1))
    channel = py5.random_choice((0, 1, 2))
    y = py5.random_int(1, h // s) * s
    px[y-s:y, :, channel] = np.roll(px[y-s:y, :, channel], direction , axis=1)
    
    direction = py5.random_choice((-1, 1))
    channel -= 1
    x = py5.random_int(1, w // s) * s
    px[:, x-s:x, channel] = np.roll(px[:, x-s:x, channel], direction, axis=0)
    #print(x, y)
    py5.set_np_pixels(px, bands='RGB')
    
def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)
