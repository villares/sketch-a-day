import py5

def setup():
    global img
    py5.size(800, 800)
    img = py5.create_graphics(1000, 1000)
    img.begin_draw()
    img.background(0, 0, 100)
    for y in range(1000):
        img.stroke(y / 4, 255 - y / 4, 128 + py5.random(-128, 128))
        img.line(0, y + py5.random(-10, 10),
                 1000, y + py5.random(-10, 10))
    img.end_draw()
    py5.no_loop()
    py5.image_mode(py5.CENTER)
    
def draw():
    py5.no_loop()
    py5.background(0)
    R = 75
    ROWS = 8
    COLS = 7
    mask = make_mask(R * 2, R * 2) 
    w = R * py5.sqrt(3)
    h = R * 1.5
    for row in range(ROWS):
        y = row * h
        for col in range(COLS):
            x = col * w
            if row % 2 == 1:
                x += w / 2 
            clipped = clip_with_mask(
                    img, mask,
                    py5.random(0, img.width - w),
                    py5.random(0, img.height - h))
            py5.image(clipped, x, y)

def make_mask(w, h):
    m = py5.create_graphics(int(w), int(h))
    m.begin_draw()
    m.fill(255)
    m.no_stroke()
    with m.begin_shape():
        for n in range(6):
            ang = (n + 0.5) * py5.TWO_PI / 6 
            x = w / 2 * py5.cos(ang) + w / 2
            y = h / 2 * py5.sin(ang) + h / 2
            m.vertex(x, y)
    m.end_draw()
    return m
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a position."""
    w, h = mask.width, mask.height
    result = py5.create_image(mask.width, mask.height, py5.ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def key_pressed():
    py5.redraw()
    py5.save_frame('###.png')

py5.run_sketch(block=False)
