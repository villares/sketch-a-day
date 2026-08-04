import py5
import numpy as np
from matplotlib import colormaps

"""
sin(sin(y)*x) + sin(sin(x)*y)
from https://mastodon.gamedev.place/@conchoid/116902524539894197
"""

def setup():
    global X, Y
    py5.size(1200, 600)
    
    x = np.linspace(-10, 20, 600)
    y = np.linspace(-10, 20, 600)
    X, Y = np.meshgrid(x, y)
    results = np.sin(np.sin(Y) * X) + np.sin(np.sin(X) * Y)
    constrained = abs(results) % 2   
    colored_array = colormaps['jet_r'](constrained) * 255
    threshold_array = (constrained > 0.25) * 255
    img1 = py5.create_image_from_numpy(colored_array, 'RGB')
    img2 = py5.create_image_from_numpy(threshold_array, 'L') 
    py5.image(img1, 0, 0)
    py5.image(img2, 600, 0)
    py5.save_frame('out.png')

py5.run_sketch(block=False)
