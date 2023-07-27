import numpy as np
import py5

img_a = img_b = img_c = None

def setup():
    global img
    py5.size(1200, 400)
    img_path = 'sample.png' # Sample from sketh 2023_07_22
    img = py5.load_image(img_path)
    img.load_np_pixels()
    print(img.np_pixels.shape)
   
def draw():
    global t
    t = py5.remap(py5.mouse_x, 0, py5.width, 0, 255)
    for i in range(3):
        img_array = img.np_pixels[:, :, i + 1]
        py5.image(apply_threshold(img_array, t, img_a), i * 400, 0, 400, 400)

def apply_threshold(img_array, threshold, dst=None):    
    new_array = np.where(img_array > threshold, 255, 0)
    return py5.create_image_from_numpy(new_array, bands='L', dst=dst)
    
def key_pressed():
    py5.save_frame(f'{t}.png')
    
py5.run_sketch()