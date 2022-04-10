# You'll need to install py5 - https://py5.ixora.io

mode_3D = False
save_pdf = False
seed = 1

s = 0.005  # noise scale


def setup():
    size(600, 600, P3D)


def draw():
    global save_pdf
    random_seed(seed)
    background(10)
    elements = []  # ((x, w, a, b), )
    margin = 50
    x = margin
    while x < 580 - margin:
        w = max(20, min(random(20, 60), 600 - margin - x))
        a = 300 * noise(1000 + x * s)
        b = 300 * noise(x * s)
        elements.append((x, w, a, b))
        x += w

    if mode_3D and not save_pdf:
        fill(255)
        lights()
        stroke(0)
        push()
        translate(width / 2, height / 4, -height)
        rotate_x(QUARTER_PI)
        rotate_z(QUARTER_PI / 2)
        translate(-width / 4, height / 2, 0)  # -height / 2, 0)

        rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, b, z=a)
        rotate_x(HALF_PI)
        rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, a, z=-b)
        pop()
    else:
        background(255)
        no_fill()
        if save_pdf:
            begin_record(PDF, 'output###.pdf')
        rect(0, 0, 600, 600)
        stroke(0, 0, 200)
        line(0, height / 2, margin, height / 2)
        for x, w, a, b in elements:
            y = 300
            stroke(200, 0, 0)
            line(x, y - a, x, y + b)
            line(x + w, y - a, x + w, y + b)
            stroke(0, 0, 200)
            line(x, y - a, x + w, y - a)
            line(x, y - a + b, x + w, y - a + b)
            line(x, y + b, x + w, y + b)
            last_x = x + w
        stroke(0, 0, 200)
        line(last_x, height / 2, width, height / 2)
        if save_pdf:
            end_record()
            save_pdf = False


def rect_h(x, y, w, h, z):
    with push_matrix():
        translate(0, 0, z)
        rect(x, y, w, h)


def rect_base(x, y, w, h, *furos):
    if furos:
        begin_shape()
        vertex(x, y)
        vertex(x + w, y)
        vertex(x + w, y + h)
        vertex(x, y + h)
        for furo in furos:
            rect_base(*furo)
        end_shape(CLOSE)
    else:
        begin_contour()
        vertex(x, y)
        vertex(x, y + h)
        vertex(x + w, y + h)
        vertex(x + w, y)
        end_contour()


def key_pressed():
    global mode_3D, save_pdf, seed
    if key == ' ':
        seed = int(random(10000))
        noise_seed(seed)
    elif key == 's':
        save_pdf = True
        print('Save PDF')
    else:
        mode_3D = not mode_3D
