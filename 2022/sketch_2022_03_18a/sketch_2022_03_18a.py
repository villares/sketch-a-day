from random import randint


def setup():
    size(800, 800)
    text_align(CENTER, CENTER)
    set_records()

def draw():
    background(100, 128, 200)
    draw_records(0, 0, width, height, records, margin=0)

def draw_records(xo, yo, wo, ho, records, **kwargs):
    margin = kwargs.pop('margin', 5)
    color_func = kwargs.pop('color_func', lambda a, ta: 255.0 * a / ta)
    x, y = xo + margin, yo + margin, 
    w, h = wo - 2 * margin, ho - 2 * margin
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for name, area, sub in records:
        color_mode(HSB)
        fill(color_func(area, total_area), 200, 200)
        if w > h:
            rw, rh = remap(area, 0, total_area, 0, w), h
        else:
            rw, rh = w, remap(area, 0, total_area, 0, h)       
        rect(x + rx, y + ry, rw, rh)
        if sub:
            draw_records(x + rx, y + ry, rw, rh, sub)
        else:
            fill(255)
            text(name, x + rx + rw /2 , y + ry + rh / 2)
        if w > h:
            rx += rw
        else:
            ry += rh

def key_pressed():
    set_records()

def r(): return randint(5, 20)

def set_records():
    global records
    records = [
    ("A", r(), []),
    ("B", r(), [
        ("BA", r(), []),
        ("BB", r(), []),
        ("BC", r(), []),
        ("BD", r(), []),
        ]),
    ("C", r(), [
        ("CA", r(), []),
        ("CB", r(), [
            ("CBA", r(), []),
            ("CBB", r(), []),            
            ]),
        ]),
    ("D", r(), []),   
    ]