from random import randint

def setup():
    size(900, 900, P3D)
    color_mode(HSB)
    stroke_weight(3)
    set_records()
    
def draw():
    background(0, 64, 50)
    lights()
    translate(width / 2, height / 2, 100)
    scale(0.5)
    rotate_x(QUARTER_PI); rotate_z(QUARTER_PI)
    translate(-width / 2, -height / 2, 0)
    draw_records(0, 0, width, height, records, margin=0)

def draw_records(xo, yo, wo, ho, records, **kwargs):
    margin = kwargs.pop('margin', 7.5)
    color_func = kwargs.pop('color_func', lambda a, ta: 255.0 * a / ta)
    x, y = xo + margin, yo + margin, 
    w, h = wo - 2 * margin, ho - 2 * margin
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for i, (name, area, sub) in enumerate(records):
        d = color_func(area, total_area)
        fill (d, 200, 200)
        if w > h:
            rw, rh = remap(area, 0, total_area, 0, w), h
        else:
            rw, rh = w, remap(area, 0, total_area, 0, h)       
        slab(x + rx, y + ry, rw, rh, d)
        if sub:
            push()
            translate(0, 0, d)
            draw_records(x + rx, y + ry, rw, rh, sub)
            pop()
        if w > h:
            rx += rw
        else:
            ry += rh

def slab(x, y, w, h, d):
    push()
    translate(x + w / 2, y + h / 2, d / 2)
    box(w, h, d)
    pop()
    
def generate_record(num, name='', max_elements=5):
    if name:
        name += '.'
    result = []
    for i in range(max_elements):
        if randint(1, 10) > 5 or num < 5:
            result.append((name + str(i), randint(1, 5), []))
        else:
            result.append((name + str(i),
                           randint(2, 10),
                           generate_record(num - 5, name + str(i))))
    return result                
 
def key_pressed():
    save_frame('###.png')
    set_records()

def set_records():
    global records
    records = generate_record(15) 
