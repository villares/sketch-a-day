import py5
import numpy as np

def setup():
    global opx
    py5.size(300, 300)
    py5.rect_mode(py5.CENTER)
    py5.rect(150, 150, 25, 25)
    opx = py5.get_np_pixels(bands='RGB')
    
def draw():
    ang = py5.mouse_x
    px = opx.copy()
    A = np.tan(np.radians(ang/2))
    B = -np.sin(np.radians(ang)) 
    for y in range(0, py5.height):
        px[y] = np.roll(px[y], int(y*A) % py5.height, axis=0)
    for x in range(0, py5.width):
        px[:, x] = np.roll(px[:, x], int(x*B), axis=0)
    for y in range(0, py5.height):
        px[y] = np.roll(px[y], int(y*A) % py5.height, axis=0)   
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)