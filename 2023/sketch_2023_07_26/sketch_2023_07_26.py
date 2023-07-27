import numpy as np
import py5

def setup():
    global array
    py5.size(600, 400)
    py5.frame_rate(10)
    array = np.zeros((py5.height, py5.width, 3), dtype=np.uint8)
    
def draw():
    start = py5.random_int(py5.height // 10) * 10
    end = start + py5.random_int(py5.height - start) // 10 * 10
    array[start:end, :, 0] = (array[start:end, :, 0] + 200) % 256
    start = py5.random_int(py5.width // 10) * 10
    end = start + py5.random_int(py5.width - start) // 10 * 10
    array[:, start:end, 1] = (array[:, start:end, 0] + 200) % 256
    start = py5.random_int(py5.height // 10) * 10
    array[start:, :, 2] = (array[start:, :, 2] + 250) % 256
    py5.set_np_pixels(array, bands='RGB')
    
py5.run_sketch()
