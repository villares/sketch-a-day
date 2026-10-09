import numpy as np
import py5

def setup():
    global img_array, buffer_img
    py5.size(800, 400)
    img_path = 'piscina.png' # Sample from sketh 2023_07_22
    img = py5.load_image(img_path)
    buffer_img = py5.create_image(img.width, img.height, py5.ARGB)  
    img.load_np_pixels()
    img_array = img.np_pixels
  
def draw():
    global threshold
    threshold = 128 # int(py5.remap(py5.mouse_y, 0, py5.height, 0, 255))
    new_array = np.where(img_array > threshold, 255, 0)
    buffer_img.set_np_pixels(new_array, bands='ARGB')
    py5.image(buffer_img, 0, 0)  # ver na tela o último resultado
  
def key_pressed():
    py5.save_frame(f'{threshold}.png')
  
py5.run_sketch()