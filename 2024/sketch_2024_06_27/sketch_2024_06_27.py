import py5
import numpy as np

def setup():
    global px, w, h
    py5.size(600, 600)
    py5.background(0, 0, 100)
    py5.rect_mode(py5.CENTER)
    py5.stroke_weight(5)
    w, h = py5.width, py5.height
    for s in range(w, 0, -20):
        py5.rect(w / 2, h / 2, s, s / w * h)
    px = py5.get_np_pixels(bands='RGB')
    
def draw():
    f = py5.frame_count // 100
    py5.random_seed(f)
    direction = py5.random_choice((-1, 1))
    
    channel = py5.random_choice((0, 1, 2))
    y = py5.random_int(h // 50) * 50
    px[y-100:y, :, channel] = np.roll(px[y-100:y, :, channel], direction , axis=1)
    
    channel = py5.random_choice((0, 1, 2))
    x = py5.random_int(w // 50) * 50
    px[:, x-100:x, channel] = np.roll(px[:, x-100:x, channel], direction, axis=0)
    
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)

