import py5

pages = []

def setup():
    global w, h
    py5.size(210 * 4, 297 * 2)
    py5.image_mode(py5.CENTER)
    w = int(py5.width / 4)
    h = int(py5.height / 2)
    f = py5.create_font('DejaVu Sans', w / 6) 
    py5.text_font(f)
    for i in range(8):
        page = py5.create_graphics(w, h)
        page.begin_draw()
        page.text_align(py5.CENTER, py5.CENTER)
        page.text_font(f)
        page.no_fill()
        page.rect(2, 2, w - 4, h - 4)
        page.fill(0)
        t = 'cover' if i == 0 else 'six' if i == 6 else str(i)
        page.text(t, w / 2, h / 2)
        page.end_draw()
        pages.append(page)
    
def draw():
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
    py5.stroke(255, 0, 0)
    py5.line(w, h, w * 3, h)
    py5.fill(255, 0, 0)
    py5.text("✂️", w + 2, h - 2)
            
def draw_page(page, x, y, rot):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(rot)
        py5.image(page, 0, 0)
        
py5.run_sketch(block=False)
