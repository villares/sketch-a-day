def setup():
    global img
    size(1440, 720)
    img = load_image('garoa.jpg')
    print(img.width, img.height)
    no_loop()
    no_stroke()
    color_mode(HSB)
    
def draw():
    background(255)
    #background(0)
    #image(img, 0, 0)
    xi, yi, wi, hi = 200, 100, 1000, 500
    passo = 5
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            xa = int(remap(x, 0, width, xi, xi + wi))
            ya = int(remap(y, 0, height, yi, yi + hi))
            c = img.get_pixels(xa , ya)
            b = brightness(c)
            fill(color(hue(c), 255, 200))
            #fill(0)
            d = 1 + passo * (255 - b) / 255
            #d = passo * b / 255
            circle(passo / 2 + x, passo / 2 + y, d)
            
    save_frame(__file__[:-3] + '.png')
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a given position."""
    w, h = mask.width, mask.height
    result = create_image(w, h, ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def g_balao_oval(w, h, draw_stroke=False):
    x, y = w / 2, h / 2
    b = create_graphics(int(w), int(h))
    b.begin_draw()
    b.clear()
    if draw_stroke:
        b.stroke_join(ROUND)
        b.stroke_weight(5)
        b.triangle(x - w * 0.45, y,
                 x, y,
                 x + w * 0.45, y + h * 0.45)
    else:
        b.no_stroke()
    b.ellipse(x, y, w * 0.9, h * 0.9)
    b.no_stroke() # triangulo sem traço para "furar" a ellipse
    # triangulo mata meia espessura, mas fica legal
    b.triangle(x - w * 0.45, y,
             x, y,
             x + w * 0.45, y + h * 0.45)
    return b



def key_pressed():
    redraw()
