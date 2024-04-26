import numpy as np
from PIL import Image
import py5

def setup():
    global temp_img
    py5.size(800, 400)
    img_path = 'piscina.png' # Sample from sketh 2023_07_22
    img = py5.load_image(img_path)
    temp_img = py5.create_image(img.width, img.height, py5.ARGB)

    #for n in range(1, 24):
    #    apply_threshold(img, n * 10)
    apply_threshold(img, 128)

def apply_threshold(img, threshold):
    img.load_np_pixels()
    img_array = img.np_pixels
    new_array = np.where(img_array > threshold, 255, 0)
    temp_img.set_np_pixels(new_array, bands='ARGB')
    temp_img.save(f'{threshold}.png')
    py5.image(temp_img, 0, 0)
    
py5.run_sketch()