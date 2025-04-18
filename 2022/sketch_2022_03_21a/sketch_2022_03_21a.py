
from random import randint, choice, seed

def setup():
    size(900, 900, P3D)
    color_mode(HSB)
    stroke_weight(3)
    seed(1)
    set_records()
    
    
def draw():
    seed(1)
    background(0, 64, 50)
    lights()
    translate(width / 2, height / 2, 100)
    scale(0.5)
    rotate_x(QUARTER_PI); rotate_z(QUARTER_PI)
    translate(-width / 2, -height / 2, 0)
    fill(200)
    rect(0, 0, width, height)
    draw_records(0, 0, width, height, records, margin=0)

def draw_records(xo, yo, wo, ho, records, **kwargs):
    z = kwargs.pop('z', 8)
    margin = choice((0, 5))
    x, y = xo + margin, yo + margin, 
    w, h = wo - 2 * margin, ho - 2 * margin
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for i, (name, area, sub) in enumerate(records):
        fill (25 * z * area / total_area, 200, 200)
        if w > h:
            rw, rh = remap(area, 0, total_area, 0, w), h
        else:
            rw, rh = w, remap(area, 0, total_area, 0, h)       
        if sub:
            push()
            translate(0, 0, z * area)
            draw_records(x + rx, y + ry, rw, rh, sub, z=z * 1.2)
            pop()
        #else:
        slab(x + rx, y + ry, rw, rh, z * area)
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
    m = millis()
    seed(m)
    print(m)
    set_records()

def set_records():
    global records
    records = generate_record(20) 
