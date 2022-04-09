# You'll need to install py5 - https://py5.ixora.io

import py5

mode_3D = False
save_pdf = False
seed = 1

s = 0.005  # noise scale


def setup():
    py5.size(600, 600, py5.P3D)

def draw():
    global save_pdf
    py5.random_seed(seed)
    py5.background(10)
    elements = []  # ((x, w, a, b), )
    margin = 50
    x = margin
    while x < 580 - margin:
        w = max(20, min(py5.random(20, 60), 600 - margin - x))
        a = 300 * py5.noise(1000 + x * s)
        b = 300 * py5.noise(x * s)
        elements.append((x, w, a, b))
        x += w

    if mode_3D and not save_pdf:
        py5.lights()
        py5.push()
        py5.translate(py5.width / 2, py5.height / 4, -py5.height)
        py5.rotate_x(py5.QUARTER_PI)
        py5.rotate_z(py5.QUARTER_PI / 2)
        py5.translate(-py5.width / 4, py5.height / 2, 0)  # -height / 2, 0)

        rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, b, z=a)
        py5.rotate_x(py5.HALF_PI)
        rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, a, z=-b)
        py5.pop()
    else:
        py5.fill(255)
        if save_pdf:
            py5.begin_record(py5.PDF, 'output###.pdf')
        py5.rect(0, 0, 600, 600)
        py5.stroke(0, 0, 200)
        py5.line(0, py5.height / 2, margin, py5.height / 2)
        for x, w, a, b in elements:
            y = 300
            py5.stroke(200, 0, 0)
            py5.line(x, y - a, x, y + b)
            py5.line(x + w, y - a, x + w, y + b)
            py5.stroke(0, 0, 200)
            py5.line(x, y - a, x + w, y - a)
            py5.line(x, y - a + b, x + w, y - a + b)
            py5.line(x, y + b, x + w, y + b)
            last_x = x + w
        py5.stroke(0, 0, 200)
        py5.line(last_x, py5.height / 2, py5.width, py5.height / 2)
        if save_pdf:
            py5.end_record()
            save_pdf = False

def rect_h(x, y, w, h, z):
    with py5.push_matrix():
        py5.translate(0, 0, z)
        py5.rect(x, y, w, h)


def rect_base(x, y, w, h, *furos):
    if furos:
        py5.begin_shape()
        py5.vertex(x, y)
        py5.vertex(x + w, y)
        py5.vertex(x + w, y + h)
        py5.vertex(x, y + h)
        for furo in furos:
            rect_base(*furo)
        py5.end_shape(py5.CLOSE)
    else:
        py5.begin_contour()
        py5.vertex(x, y)
        py5.vertex(x, y + h)
        py5.vertex(x + w, y + h)
        py5.vertex(x + w, y)
        py5.end_contour()


def key_pressed():
    global mode_3D, save_pdf, seed
    if py5.key == ' ':
        seed = int(py5.random(10000))
        py5.noise_seed(seed)
    elif py5.key == 's':
        save_pdf = True
        print('Save PDF')
    else:
        mode_3D = not mode_3D

py5.run_sketch()
