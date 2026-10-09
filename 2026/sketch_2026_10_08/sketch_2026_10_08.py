import numpy as np
import py5

def setup():
    py5.size(800, 400)
    py5.background(0)
    img_path = 'piscina.png' 
    img = py5.load_image(img_path)
    img.load_np_pixels()
    print(img.np_pixels.shape)
    pa = img.np_pixels
    pa[::2, 400:, 1:3] = 255
    pa[:, ::2, 2] = 0
    pa[1::2, 200:600, 3] = 0

    img.update_np_pixels()
    py5.image(img, 0, 0)
    
    py5.save_frame(f'out1.png')
  
py5.run_sketch()
