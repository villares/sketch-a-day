import py5
import numpy as np

def setup():
    py5.size(900, 600)
    w, h = py5.width, py5.height
    R = np.linspace(0, 255, w).reshape(1, -1)
    G = np.linspace(0, 255, h).reshape(-1, 1)
    B = np.random.uniform(128, 255, (h, w))
    A = np.array([[128 + py5.dist(w /2, h / 2, x, y) % 128
                   for x in range(w)]
                   for y in range(h)])
    rgba = np.dstack(np.broadcast_arrays(R, G, B, A))
    img = py5.create_image_from_numpy(rgba, 'RGBA');
    py5.image(img, 0, 0)
    
py5.run_sketch()
