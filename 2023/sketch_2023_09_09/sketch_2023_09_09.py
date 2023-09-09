import py5
import numpy as np

from itertools import chain, product

w = 100
n = 6
pad = 5


def setup():
    py5.size(600, 600)
    generate_faces()

def generate_faces():
    global faces
    grid = {
        (i, j): (w / 2 + i * w + py5.random(-10, 10),
                 w / 2 + j * w + py5.random(-10, 10))
        for i, j in product(range(n), range(n))
    } 
    face_list = []        
    for i, j in product(range(n - 1), repeat=2):
        a, b, c, d = (
            grid[(i, j)],
            grid[(i + 1, j)],
            grid[(i + 1, j + 1)],
            grid[(i, j + 1)],
        )
        face_list.append((
            (a[0] + pad, a[1] + pad),
            (b[0] - pad, b[1] + pad),
            (c[0] - pad, c[1] - pad),
            (d[0] + pad, d[1] - pad),
        ))
    faces = np.array(face_list)

def bounding_box(vs):
    x_min, y_min = np.min(vs, axis=0)
    x_max, y_max = np.max(vs, axis=0)
    return (x_min, y_min), (x_max, y_max)

def draw():
    py5.background(150, 150, 250)
    py5.fill(255)
    with py5.begin_shape(py5.QUADS):
        py5.vertices(list(chain(*faces)))
    py5.rect_mode(py5.CORNERS)
    py5.fill(255, 0, 0, 100)
    for f in faces:
        (min_x, min_y), (max_x, max_y) = bounding_box(f)
        py5.rect(min_x, min_y, max_x, max_y)

def key_pressed():
    generate_faces()


py5.run_sketch()
