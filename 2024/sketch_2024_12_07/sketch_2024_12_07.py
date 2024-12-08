import numpy as np
import py5
from skimage import measure
from skimage.segmentation import slic
from skimage.data import astronaut
from skimage.color import label2rgb

astronaut_image = astronaut()
astronaut_segments = slic(astronaut_image,
                          n_segments=100,
                          compactness=10) * 10 % 255

def setup():
    global img
    py5.size(512, 512)
    py5.color_mode(py5.HSB)
    img = py5.create_image_from_numpy(astronaut_segments, 'L')

#def draw():
    py5.image(img, 0, 0)
    t = py5.mouse_x / py5.width * 255
    py5.image(img, 0, 0)
    py5.save('out.png')

py5.run_sketch(block=False)