import py5
import numpy as np

def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    py5.no_loop()
    
def draw():
    py5.rect(250, 250, 250, 125)
    px = py5.get_np_pixels(bands='RGB')
    for y in range(py5.height):
        px[y] = np.roll(px[y], y, axis=0)
    py5.set_np_pixels(px, bands='RGB')
    
py5.run_sketch(block=False)