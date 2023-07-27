import numpy as np
from PIL import Image
import py5

def setup():
    global temp_img
    py5.size(800, 800)
    img_path = 'sample.png' # Sample from sketh 2023_07_22
    img = py5.load_image(img_path)
    temp_img = py5.create_image(img.width, img.height, py5.RGB)

    for n in range(1, 24):
        apply_threshold(img, n * 10)


def apply_threshold(img, threshold):
    img.load_np_pixels()
    img_array = img.np_pixels
    new_array = np.where(img_array > threshold, 255, 0)
    temp_img.set_np_pixels(new_array, bands='RGB')
    temp_img.save(f'{threshold}.png')

    
py5.run_sketch()