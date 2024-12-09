import py5

from skimage.data import astronaut

astronaut_image = astronaut()

def setup():
    global img
    py5.size(512, 512)
    py5.color_mode(py5.HSB)
    img = py5.create_image_from_numpy(astronaut_image, 'RGB')

#def draw():
    py5.image(img, 0, 0)
    py5.save('astronaut.png')

py5.run_sketch(block=False)