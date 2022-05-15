from random import randint, choice


def setup():
    global records
    size(900, 900)
    text_align(CENTER, CENTER)
    text_size(8)
    text_font(create_font("Courier", 20))
    records = generate_records("")
    no_loop()
    
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
            next_sub = choice((1, 0)) if rw * rh > 10000 else 0
            next_records =  generate_records(name, next_sub)
            draw_records(x + rx, y + ry, rw, rh, next_records)
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

def generate_records(name, next_sub=True):
    if name: name += '/'
    return [(name + next_name, randint(1, 5), next_sub) for next_name in 'ABCDEF']

def key_pressed():
    global records
    save_frame('###.png')
    records = generate_records("")
    redraw()

         
