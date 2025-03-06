import py5
import numpy as np

def setup():
    global offscreen, circular_mask
    py5.size(600, 300)
    offscreen = py5.create_graphics(200, 200)  # Py5Graphics (an offscreen canvas)
    offscreen.begin_draw()
    for _ in range(200):
        offscreen.fill(255, 64)
        offscreen.square(py5.random(200), py5.random(200), 20) 
    offscreen.end_draw()
    circular_mask = py5.create_graphics(200, 200)  # Py5Graphics
    circular_mask.begin_draw()
    circular_mask.fill(255)
    circular_mask.circle(100, 100, 200)
    circular_mask.end_draw()

def draw():
    py5.background(0, 0, 100)
    py5.fill(255, 0, 0)
    # normal .mask() doesn't preserve offscreen canvas alpha
    img = offscreen.copy()  # Py5Graphics copies are Py5Image
    img.mask(circular_mask)
    py5.square(100, 50, 100)
    py5.image(img, 100, 50)
    # this preserves the offscreen canvas alpha
    mask_preserving_alpha(offscreen, circular_mask)
    py5.square(300, 50, 100)
    py5.image(offscreen, 300, 50)
    
def mask_preserving_alpha(img, mask):
    mask.load_np_pixels()
    img.load_np_pixels()
    img_alpha = img.np_pixels.copy()[:, :, 0]
    img.np_pixels[:, :, 0] = np.where(mask.np_pixels[:, :, 0] < img_alpha,
                                      mask.np_pixels[:, :, 0], img_alpha)
    img.update_np_pixels()
    
py5.run_sketch(block=False)
    