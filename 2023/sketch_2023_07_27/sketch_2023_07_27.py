import numpy as np
import py5

def setup():
    global array
    py5.size(600, 400)
    py5.frame_rate(10)
    array = np.zeros((py5.height, py5.width, 3), dtype=np.uint8)
    
def draw():
    w, h = py5.random_int(10) * 10, py5.random_int(10) * 10
    x, y = py5.random_int(py5.width - w) // 10 * 10, py5.random_int(py5.height - h) // 10 * 10
    array[y:y+h, x:x+w, 0] = (array[y:y+h, x:x+w, 0] + 200) % 256
    start = py5.random_int(py5.width) // 10 * 10
    end = start + py5.random_int(py5.width - start) // 10 * 10
    array[:, start:end, 1] = (array[:, start:end, 1] + 200) % 256
    start = py5.random_int(py5.height // 10) * 10
    array[start:, :, 2] = (array[start:, :, 2] + 250) % 256
    py5.set_np_pixels(array, bands='RGB')
 
def key_pressed():
    py5.save_frame('###.png')
 
py5.run_sketch(block=False)
