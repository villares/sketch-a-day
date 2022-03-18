records = [
    ("A", 30, []),
    ("B", 10, [
        ("BA", 30, []),
        ("BB", 10, []),
        ("BC", 50, []),
        ("BD", 20, []),
        ]),
    ("C", 50, [
        ("CA", 30, []),
        ("CB", 10, [
            ("CBA", 30, []),
            ("CBB", 10, []),            
            ]),
        ]),
    ("D", 20, []),   
    ]

MARGIN = 5

def setup():
    size(600, 400)
    text_align(CENTER, CENTER)

def draw():
    background(100, 128, 200)
    draw_records(MARGIN, MARGIN,
                 width - 2 * MARGIN, height - 2 * MARGIN, records)

def draw_records(x, y, w, h, records, hor=True):
    total_area = sum(map(lambda r: r[1], records))
    rx = ry = 0
    for name, area, sub in records:
        fill(128 + area % 128, 150)
        if w > h:
            rw, rh = remap(area, 0, total_area, 0, w), h
        else:
            rw, rh = w, remap(area, 0, total_area, 0, h)       
        rect(x + rx, y + ry, rw, rh)
        if sub:
            draw_records(x + rx + MARGIN, y + ry + MARGIN,
                         rw - 2 * MARGIN, rh - 2 * MARGIN, sub)
        else:
            fill(255)
            text(name, x + rx + rw /2 , y + ry + rh / 2)
        if w > h:
            rx += rw
        else:
            ry += rh