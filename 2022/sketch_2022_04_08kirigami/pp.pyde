# for Processing Python Mode
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

add_library('pdf')
mode_3D = False
save_pdf = False
seed = 1

s = 0.005  # noise scale

def setup():
    size(600, 600, P3D)


def draw():
    global save_pdf
    randomSeed(seed)
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
        push()
        translate(width / 2, height / 4, -height)
        rotateX(QUARTER_PI)
        rotateZ(QUARTER_PI / 2)
        translate(-width / 4, height / 2, 0)  # -height / 2, 0)

        rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, b, z=a)
        rotateX(HALF_PI)
        rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elements])
        for x, w, a, b in elements:
            rect_h(x, 0, w, a, z=-b)
        pop()
    else:
        background(255)
        noFill()
        if save_pdf:
            beginRecord(PDF, 'output###.pdf')
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
            endRecord()
            save_pdf = False

def rect_h(x, y, w, h, z):
    with pushMatrix():
        translate(0, 0, z)
        rect(x, y, w, h)


def rect_base(x, y, w, h, *furos):
    if furos:
        beginShape()
        vertex(x, y)
        vertex(x + w, y)
        vertex(x + w, y + h)
        vertex(x, y + h)
        for furo in furos:
            rect_base(*furo)
        endShape(CLOSE)
    else:
        beginContour()
        vertex(x, y)
        vertex(x, y + h)
        vertex(x + w, y + h)
        vertex(x + w, y)
        endContour()


def keyPressed():
    global mode_3D, save_pdf, seed
    if key == ' ':
        seed = int(random(10000))
        noiseSeed(seed)
    elif key == 's':
        save_pdf = True
        print('Save PDF')
    else:
        mode_3D = not mode_3D

