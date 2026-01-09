import py5

def setup():
    py5.size(900, 900, py5.P3D)
    py5.color_mode(py5.CMAP, 'viridis_r', 255)
    py5.stroke_weight(3)
    py5.random_seed(1)
    set_records()
    
def draw():
    #py5.random_seed(1)
    py5.background(255)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2, 100)
    py5.scale(0.5)
    py5.rotate_x(py5.QUARTER_PI)
    py5.rotate_z(py5.QUARTER_PI)
    py5.translate(-py5.width / 2, -py5.height / 2, 0)
    draw_records(0, 0, py5.width, py5.height, records)

def draw_records(xo, yo, wo, ho, records, **kwargs):
    z = kwargs.pop('z', 8)
    x, y = xo + margin, yo + margin, 
    w, h = wo - 2 * margin, ho - 2 * margin
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for i, (name, area, sub) in enumerate(records):
        py5.fill (25 * z * area / total_area)
        if w > h:
            rw, rh = py5.remap(area, 0, total_area, 0, w), h
        else:
            rw, rh = w, py5.remap(area, 0, total_area, 0, h)       
        if sub:
            with py5.push():
                py5.translate(0, 0, z * area)
                draw_records(x + rx, y + ry, rw, rh, sub, z=z * 1.2)
        #else:
        slab(x + rx, y + ry, rw, rh, z * area)
        if w > h:
            rx += rw
        else:
            ry += rh

def slab(x, y, w, h, d):
    with py5.push():
        py5.translate(x + w / 2, y + h / 2, d / 2)
        py5.box(w, h, d)
        
def generate_record(num, name='', max_elements=5):
    if name:
        name += '.'
    result = []
    for i in range(max_elements):
        if py5.random_int(1, 10) > 5 or num < 5:
            result.append((name + str(i), py5.random_int(1, 5), []))
        else:
            result.append((name + str(i),
                           py5.random_int(2, 10),
                           generate_record(num - 5, name + str(i))))
    return result                
 
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    f = py5.frame_count
    py5.random_seed(f)
    print(f)
    set_records()

def set_records():
    global records, margin
    margin = py5.random_choice((0, 5))
    records = generate_record(20) 

py5.run_sketch(block=False)