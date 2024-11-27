
def setup():
    global img_c
    size(446, 454)
    img_a = load_image('xfce.png')
    img_b = load_image('manjaro.png')
    img_c = create_graphics(width, height)
    H = 10
    img_c.begin_draw()
    for y in range(0, height, H * 2):
        ra = img_a.get_pixels(0, y, width, H)
        image(ra, 0, y)
        rb = img_b.get_pixels(0, y + H, width, H)
        image(rb, 0, y + H)
    img_c.end_draw()
    
def draw():
    image(img_c, 0, 0)


