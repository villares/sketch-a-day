from random import randint

def setup():
    size(900, 900)
    text_align(CENTER, CENTER)
    text_size(8)
    set_records()
    text_font(create_font("Courier", 20))
    
def draw():
    background(100, 128, 200)
    draw_records(0, 0, width, height, records, margin=0)

def draw_records(xo, yo, wo, ho, records, **kwargs):
    margin = kwargs.pop('margin', 7.5)
    color_func = kwargs.pop('color_func', lambda a, ta: 200 - 255.0 * a / ta)
    x, y = xo + margin, yo + margin, 
    w, h = wo - 2 * margin, ho - 2 * margin
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for i, (name, area, sub) in enumerate(records):
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
            fill(0)
            ts = 5
            text_size(ts)
            while text_width(name) < rw - 4 and ts < rh / 3:
                ts += 1
                text_size(ts)                
            if ts != 5:
                text(name, x + rx + rw /2 , y + ry + rh / 2)
        if w > h:
            rx += rw
        else:
            ry += rh

def key_pressed():
    save_frame('###.png')
    set_records()

def set_records():
    global records
    records = generate_record(15) 
    
def generate_record(num, name='', max_elements=5):
    if name:
        name += '.'
    result = []
    for i in range(max_elements):
        if randint(1, 10) > 5 or num < 5:
            result.append(
                (name + str(i), randint(1, 5), [])
            )
        else:
            result.append(
                (
                name + str(i),
                randint(2, 10),
                generate_record(num - 5, name + str(i))
                )
            )
    return result            