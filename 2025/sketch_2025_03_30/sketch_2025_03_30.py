import py5

def setup():
    global img
    py5.size(800, 800)
    img = py5.create_graphics(1000, 1000)
    img.begin_draw()
    img.background(128)
    img.no_fill()
    for x in range(0, 1500, 10):
        for y in range(0, 1500, 10):
            img.stroke(y / 20,
                       py5.random(0, 128),
                       py5.random(0, 255), 128)
            img.circle(500, y + py5.random(-15, 15), 1000)
            img.stroke(x / 20,
                       py5.random(128, 255),
                       py5.random(128, 255), 128)
            img.circle(x + py5.random(-15, 15), 500, 1000)
    img.end_draw()
    py5.no_loop()
    py5.image_mode(py5.CENTER)
    
def draw():
    py5.no_loop()
    py5.background(0, 0, 100)
    R = 45
    w = R * 1.5
    h = R * py5.sqrt(3)
    ROWS = int(py5.height / h) + 1
    COLS = int(py5.width / w) * 2 + 2
    mask = make_mask(R * 2, R * 2, pointy=False) 
    for col in range(COLS):
        x = col * w / 2
        for row in range(ROWS):
            y = row * h 
            if col % 2 == 1:
                y += h / 2 
            clipped = clip_with_mask(
                    img, mask,
                    py5.random(0, img.width - w),
                    py5.random(0, img.height - h))
            with py5.push_matrix():
                py5.translate(x, y)
                #py5.rotate(py5.random_int(6) * py5.TWO_PI / 6)
                py5.image(clipped, 0, 0)
#     py5.image(img, 400, 400, 800, 800) # test/debug!
    py5.save_frame('###.png')

def make_mask(w, h, pointy=False):
    m = py5.create_graphics(int(w), int(h))
    m.begin_draw()
    m.fill(255)
    m.no_stroke()
    with m.begin_shape():
        for n in range(6):
            ang = (n + 0.5 * pointy) * py5.TWO_PI / 6 
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

py5.run_sketch(block=False)

