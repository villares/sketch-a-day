import py5
import numpy as np

from itertools import chain, product

w = 200
n = 5
pad = 5
passo = 12

def setup():
    global img
    py5.size(800, 800)
    generate_faces()
    foto = py5.load_image('garoa.jpg')
    py5.color_mode(py5.RGB)
    img = draw_base(foto)
    py5.no_loop()

def generate_faces():
    global faces
    grid = {
        (i, j): (int(i * w + ((py5.random(-10, 10)) if (i != 0 and i != n-1) else 0)),
                 int(j * w + ((py5.random(-10, 10)) if (j != 0 and j != n-1) else 0)))
        for i, j in product(range(n), range(n))
    }
    print(grid)
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
    py5.background(255)
    for f in faces:
        (min_x, min_y), (max_x, max_y) = bounding_box(f)
        w = max_x - min_x
        h = max_y - min_y
        fc = f.copy()
        fc -= np.array((min_x, min_y)) # translate to origin   
        m = make_mask(fc, w, h)
        rx, ry = py5.random(img.width - w), py5.random(img.height - h)
        clipped = clip_with_mask(img, m, rx, ry)
        py5.image(clipped, min_x, min_y)
    # the blue borders        
    py5.no_fill()
    py5.stroke_weight(3)
    py5.stroke(0, 0, 200)
    with py5.begin_shape(py5.QUADS):
        py5.vertices(list(chain(*faces)))


def make_mask(face_points, w, h):
    pg = py5.create_graphics(w, h)
    pg.begin_draw()
    pg.no_stroke()
    pg.begin_shape()
    pg.vertices(face_points)
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

    
def draw_base(base):
    pg = py5.create_graphics(base.width, base.height)
    pg.begin_draw()
    pg.background(0)
    xi, yi, wi, hi = 200, 100, 10, 500
    for x in range(0, pg.width, passo):
        for y in range(0, pg.height, passo):
            c = base.get_pixels(x, y)
            b = py5.brightness(c)
            s =  py5.color(py5.hue(c), 255, 200)
            d = b * passo / 255
            pg.fill(255)
            pg.no_stroke()
            pg.circle(passo / 2 + x, passo / 2 + y, d)
    pg.end_draw()
    return pg

                 
def elemento(x, y, b, s):
    py5.rect_mode(py5.CENTER)
    py5.fill(s)
    d = passo * b / 255 + 2
    t = ' -+*108'[int(d) // 2]
    py5.text_size(14)
    py5.text(t, x, y)
#     rect(x, y, w, w / 3)
#     rect(x, y, w / 3, w)


def key_pressed():
    generate_faces()
    py5.save_frame('###.png')
    py5.redraw()


py5.run_sketch(block=False)
