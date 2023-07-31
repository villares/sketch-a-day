import py5

pages = []
save_pdf = False

def setup():
    global w, h, f
    py5.size(210 * 4, 297 * 2)
    py5.text_mode(py5.SHAPE)
    w = int(py5.width / 4)
    h = int(py5.height / 2)
    f = py5.create_font('DejaVu Sans', 100) 
    for i in range(8):
        page = py5.create_graphics(w * 5, h * 5)
        page.begin_draw()
        page.text_align(py5.CENTER, py5.CENTER)
        page.text_font(f)
        page.text_size(page.width / 8)
        page.text_mode(py5.SHAPE)
        page.no_fill()
        #page.rect(2, 2, w - 4, h - 4)
        page.color_mode(py5.HSB)
        page.no_stroke()
        for _ in range(1000):
            b = py5.random_int(50, 100)
            page.fill(i * 24, 200, b * 2)
            page.circle(py5.random_int(w * 5), py5.random_int(h * 5), b)
        page.fill(255)
        t = 'cover' if i == 0 else 'six' if i == 6 else str(i)
        page.text(t, page.width - w, page.height - h)
        page.end_draw()
        pages.append(page.copy())
    
def draw():
    global save_pdf
    if save_pdf:
        pdf = py5.create_graphics(py5.width, py5.height, py5.PDF, 'out.pdf')
        py5.begin_record(pdf)
    py5.image_mode(py5.CENTER)
    x = w / 2
    y = h / 2
    r = -py5.PI
    for i in (0, 7, 6, 5, 1, 2, 3, 4):
        draw_page(pages[i], x, y, r)
        #py5.text(str(i), x, y)
        x += w
        if x > py5.width:
            x = w / 2
            y += h
            r = 0
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.line(w, h, w * 3, h)
    py5.fill(255)
    py5.text_font(f)
    py5.text_size(w / 6)
    py5.text("✂️", w + 2, h - 2)
    if save_pdf:
        py5.end_record()
        save_pdf = False



def draw_page(page, x, y, rot):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(rot)
        py5.image(page, 0, 0, w, h)

def key_pressed():
    global save_pdf
    save_pdf = True

py5.run_sketch(block=False)
