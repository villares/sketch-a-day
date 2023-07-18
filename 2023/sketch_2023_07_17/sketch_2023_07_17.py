
def setup():
    global source, clipped
    size(600, 600)
    source = load_image('a.png')
    mask = create_graphics(300, 200)
    w, h = mask.width, mask.height
    mask.begin_draw()
    mask.ellipse(w / 2, h / 2, w, h)
    mask.end_draw()
    clipped = clip_image(source, mask, 300, 300, mode=CENTER)

def clip_image(img, mask, x, y, mode=CORNER):
    w, h = mask.width, mask.height
    if mode == CORNER:
        xs, yx = x, y
    else:
        xs, ys = int(x - w / 2), int(y - h / 2)
        
#     result = create_graphics(w, h) #, ARGB)
#     result.begin_draw()
#     result.copy(img, xs, ys, w, h, 0, 0, w, h)
#     result.mask(mask)
#     result.end_draw()
    result = create_image(w, h, ARGB)
    result.copy(img, xs, ys, w, h, 0, 0, w, h)
    result.mask(mask)
    
    return result

def draw():
    background(200)
    image_mode(CORNER)
    image(source, 0, 0)
    apply_filter(BLUR, 4)
    image_mode(CENTER)
    image(clipped, 150, 100)


