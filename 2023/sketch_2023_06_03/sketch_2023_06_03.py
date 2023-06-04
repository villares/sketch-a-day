import py5
import numpy as np

def setup():
    global npa, dst
    py5.size(600, 600)
    npa = np.empty((py5.width, py5.height)).T
    npa.fill(100)
    dst = dist_to_pos(py5.width, py5.height, 300, 300)
    
def draw():
    rnd = np.random.randint(0, 300, size=(py5.width, py5.height)).T
    img = dst < rnd
    py5.set_np_pixels(npa + img * 150, 'L')

def dist_to_pos(width, height, cx, cy):
    """ reeturns a 2D array filled with distances """
    x = np.arange(width)
    y = np.arange(height)
    xx, yy = np.meshgrid(x, y)
    return np.linalg.norm(np.array([xx - cx, yy - cy]), axis=0)

py5.run_sketch()