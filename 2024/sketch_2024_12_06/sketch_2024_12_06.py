import numpy as np
import py5
from skimage import measure

# from https://scikit-image.org/docs/stable/auto_examples/edges/plot_contours.html
x, y = np.ogrid[-np.pi : np.pi : 400j, -np.pi : np.pi : 400j]
r = np.sin(np.exp(np.sin(x) ** 3 + np.cos(y) ** 2))
r = r.T
r *= 255

def setup():
    global img
    py5.size(400, 400)
    py5.color_mode(py5.HSB)
    img = py5.create_image_from_numpy(r.T, 'L')

def draw():
    py5.image(img, 0, 0)
    t = py5.mouse_x / py5.width * 255
    contours = measure.find_contours(r, t)

    for i, contour in enumerate(contours):
        py5.fill(i * 32, 255, 255, 150)
        with py5.begin_closed_shape():
            py5.vertices(contour)

py5.run_sketch(block=False)