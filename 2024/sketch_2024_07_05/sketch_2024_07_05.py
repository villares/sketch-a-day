from itertools import product

import py5, py5_tools
import numpy as np

def setup():
    global px, w, h
    py5.size(500, 500)
    w, h = py5.width, py5.height
    py5.background(255)
    py5.fill(0)
    for x, y in product(range(50, 500, 100), repeat=2):
        py5.circle(x, y, 75)
    px = py5.get_np_pixels(bands='RGB')
    py5_tools.animated_gif('out.gif', count=200, period=0.2, duration=0.2)

    
def draw():
    f = py5.frame_count // 100
    py5.random_seed(f)
    
    direction = py5.random_choice((-1, 1))
    channel = py5.random_choice((0, 1, 2))
    y = py5.random_int(1, h // 100) * 100
    px[y-100:y, :, channel] = np.roll(px[y-100:y, :, channel], direction , axis=1)
    
    direction = py5.random_choice((-1, 1))
    channel -= 1
    x = py5.random_int(1, w // 100) * 100
    px[:, x-100:x, channel] = np.roll(px[:, x-100:x, channel], direction, axis=0)
    print(x, y)
    py5.set_np_pixels(px, bands='RGB')
    
def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)
