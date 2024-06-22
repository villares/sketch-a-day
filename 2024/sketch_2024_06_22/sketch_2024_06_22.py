import py5
import numpy as np

def setup():
    global opx
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    py5.rect(250, 250, 250, 125)
    opx = py5.get_np_pixels(bands='RGB')
    
def draw():
    ang = py5.mouse_x
    px = opx.copy()
    A = np.tan(np.radians(ang/2)) / 10
    B = -np.sin(np.radians(ang)) / 10
    for y in range(-py5.height//2, py5.height//2):
        px[y] = np.roll(px[y], int(y*A) % py5.height, axis=0)
    for x in range(-py5.width//2, py5.width//2):
        px[:, x] = np.roll(px[:, int(x*B) % py5.width], x, axis=0)
    for y in range(-py5.height//2, py5.height//2):
        px[y] = np.roll(px[y], int(y*A) % py5.height, axis=0)   
    py5.set_np_pixels(px, bands='RGB')

def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=False)