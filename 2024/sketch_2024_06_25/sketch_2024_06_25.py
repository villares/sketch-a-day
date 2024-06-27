import py5
import numpy as np

def setup():
    global px
    py5.size(500, 500)
    py5.background(0, 0, 100)
    py5.rect_mode(py5.CENTER)
    for s in range(350, 0, -10):
        py5.square(250, 250, s)
    px = py5.get_np_pixels(bands='RGB')
    
def draw():
    f = py5.frame_count // 100
    py5.random_seed(f)
    direction = 1 #py5.random_choice((-1, 1))
    y = py5.random_int(py5.height // 50) * 50
    px[y-100:y] = np.roll(px[y-100:y], direction , axis=1)
    x = py5.random_int(py5.width // 50) * 50
    px[:, x-100:x] = np.roll(px[:, x-100:x], direction, axis=0)
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)