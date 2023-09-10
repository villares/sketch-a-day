import py5
import numpy as np

from itertools import chain, product

w = 100
n = 6
pad = 5


def setup():
    global img
    py5.size(600, 600)
    generate_faces()
    img = py5.load_image('a.png')
    py5.no_loop()

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
    py5.background(150)
    #py5.rect_mode(py5.CORNERS)
    for f in faces:
        bb = bounding_box(f)
        (min_x, min_y), (max_x, max_y) = bb
        w = max_x - min_x
        h = max_y - min_y
        m = make_mask(f)
        rx, ry = py5.random(img.width - w), py5.random(img.height - h)
        clipped = clip_with_mask(img, m, rx, ry)
        py5.image(clipped, min_x, min_y)
    py5.no_fill()
    py5.stroke_weight(3)
    py5.stroke(0, 0, 200)
    #py5.translate(-1, -1)
    with py5.begin_shape(py5.QUADS):
        py5.vertices(list(chain(*faces)))

        
def make_mask(f):
    global fc
    fc = f.copy()
    (min_x, min_y), (max_x, max_y) = bounding_box(f)
    fc[:,0] -= min_x
    fc[:,1] -= min_y
    w = max_x - min_x
    h = max_y - min_y
    pg = py5.create_graphics(int(w), int(h))
    pg.begin_draw()
    pg.no_stroke()
    pg.begin_shape()
    pg.vertices(fc)
    pg.end_shape()
    pg.end_draw()
    return pg



def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a given position."""
    w, h = mask.width, mask.height
    result = py5.create_image(int(w), int(h), py5.ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result


def key_pressed():
    generate_faces()
    py5.redraw()


py5.run_sketch(block=False)
