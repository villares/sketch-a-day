import numpy as np
import py5

def setup():
    py5.size(800, 400)
    py5.background(0)
    img_path = 'piscina.png' 
    img = py5.load_image(img_path)
    img.load_np_pixels()
    print(img.np_pixels.shape) # (400, 800, 4)    
    pa = img.np_pixels
    pa[pa > 128] = 255
    pa[pa < 128] = 0   
    #pa[:, :, 1] = 255
    #pa[:, :, 1] = 0
    #pa[:, :, 2] = 0  # zero greens
    img.update_np_pixels()
    py5.image(img, 0, 0)
    py5.save_frame(f'saturated.png')
  
py5.run_sketch()
