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
    background(0)
    #image(img, 0, 0)
    xi, yi, wi, hi = 200, 100, 1000, 500
    passo = 15
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            xa = int(remap(x, 0, width, xi, xi + wi))
            ya = int(remap(y, 0, height, yi, yi + hi))
            c = img.get_pixels(xa , ya)
            b = brightness(c)
            fill(color(hue(c), 255, 200))
            #d = 1 + passo * (255 - b) / 255
            d = passo * b / 255
            mais(passo / 2 + x, passo / 2 + y, 2 + d)
            
    save_frame(__file__[:-3] + '.png')
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a given position."""
    w, h = mask.width, mask.height
    result = create_image(w, h, ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def mais(x, y, w):
    rect_mode(CENTER)
    rect(x, y, w, w / 3)
    rect(x, y, w / 3, w)



def key_pressed():
    redraw()

