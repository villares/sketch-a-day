
def setup():
    global img_c
    size(446, 454)
    img_a = load_image('xfce.png')
    img_b = load_image('manjaro.png')
    img_c = create_graphics(width, height)
    H = 10
    img_c.begin_draw()
    cols = width // H
    rows = height // H
    for i in range(cols):
        x = i * H
        for j in range(rows):
            y = j * H
            if (i + j) % 2:
                img = img_a.get_pixels(x, y, H, H)
            else:
                img = img_b.get_pixels(x, y, H, H)
            image(img, x, y)            
    img_c.end_draw()
    
def draw():
    image(img_c, 0, 0)
    
def key_pressed():
    save_frame('out.png')


