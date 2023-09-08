from functools import cache

passo = 9
stats = set()

def setup():
    global img
    size(1440, 720)
    img = load_image('garoa.jpg')
    print(img.width, img.height)
    no_loop()
    no_stroke()
    color_mode(HSB)
    text_font(create_font('Inconsolata Bold', 10))
    text_align(CENTER, CENTER)
    
def draw():
    background(0)
    #image(img, 0, 0)
    xi, yi, wi, hi = 200, 100, 1000, 500
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            xa = int(remap(x, 0, width, xi, xi + wi))
            ya = int(remap(y, 0, height, yi, yi + hi))
            c = img.get_pixels(xa , ya)
            b, s = brightness_and_saturated(c)
            elemento(passo / 2 + x, passo / 2 + y, b, s)
            
    save_frame(__file__[:-3] + '.png')
    print(len(stats), stats)

         
@cache
def brightness_and_saturated(c):
    return brightness(c), color(hue(c), 255, 200)
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a given position."""
    w, h = mask.width, mask.height
    result = create_image(w, h, ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def elemento(x, y, b, s):
    rect_mode(CENTER)
    fill(s)
    d = passo * b / 255 + 2
    stats.add(int(d) // 2)
    t = ' -+*108'[int(d) // 2]
    text_size(14)
    text(t, x, y)
#     rect(x, y, w, w / 3)
#     rect(x, y, w / 3, w)

def key_pressed():
    redraw()

