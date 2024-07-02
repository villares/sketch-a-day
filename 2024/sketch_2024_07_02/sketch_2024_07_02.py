import py5
import py5_tools
import numpy as np

def setup():
    py5.size(600, 600)
    start()
    py5_tools.animated_gif('out.gif', count=150, period=0.2, duration=0.2)

def start():
    global px, w, h
    py5.background(0)
    py5.stroke_weight(5)
    py5.no_stroke()
    w, h = py5.width, py5.height
    for i, x in enumerate(range(0, w, 20)):
        py5.fill((0, 255)[i % 2])
        py5.rect(x, 0, 20, h)
    px = py5.get_np_pixels(bands='RGB')
    
def draw():
    f = (py5.frame_count - 1) // 100
    py5.random_seed(f)
    direction = py5.random_choice((-1, 1))
    
    channel = py5.random_choice((0, 1, 2))
    y = py5.random_int(h // 100) * 100
    px[y-100:y, :, channel] = np.roll(px[y-100:y, :, channel], direction , axis=1)
    
    #channel = py5.random_choice((0, 1, 2))
    #channel -= 1
    x = py5.random_int(w // 100) * 100
    px[:, x-100:x, channel] = np.roll(px[:, x-100:x, channel], direction, axis=0)
    
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')
    start()

py5.run_sketch(block=False)
