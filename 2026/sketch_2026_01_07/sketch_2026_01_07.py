# The cool binary XOR based pattern I learned fron Ntsutae

from itertools import product

import py5
import numpy as np

a = 2
b = 1024
c = 256
m = 0

def setup():
    global xys
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
#     py5_tools.animated_gif(
#         'out2.gif',
#         frame_numbers=range(1, 361, 5),
#         duration=0.16
#    )
    pxs = py5.get_np_pixels()
    print(pxs.shape)
    xys = np.array(tuple(product(range(800), range(800))))

def draw():
#     py5.background(255)  
#     t = 0 # py5.frame_count
#     for y in range(py5.height):
#         for x in range(py5.width):
#             v = abs((x + y - t) ^ (x - y + t))
#             test = (m * 100 + pow(v, a)) % b;
#             if test < c:
#                 py5.point(x, y)
    t = py5.frame_count
    pxs = np.ones((py5.height, py5.width, 3),
                  dtype=np.uint8) * 255 
    v = np.abs((x + y - t) ^ (x - y + t))
    mask = ((m * 100 + np.power(v, a)) % b) < c       
    pxs[mask, :3] = (0, 0, 0)     
    py5.set_np_pixels(pxs, bands='RGB')
    
def key_pressed():
    global a, m
    if py5.key == 'a':
        a +=  1
    elif py5.key == 'z':
        a -= 1
    elif py5.key == 's':
        m += 1
    elif py5.key == 'x':
        m -= 1
    elif py5.key == 'p':
        py5.save_frame('###.png')
  
    
py5.run_sketch(block=False)

