def setup():
    size(400, 200)
    background(200)
    image_mode(CENTER)
    sb = speech_bubble(300, 200)
    img = load_image('a.png')
    clipped = fill_and_clip(sb, img, 300, 300, mode=CENTER)
    image(clipped, 150, 100)
     
def fill_and_clip(mask: Py5Graphics, img_fill: Py5Image, x, y, mode=CORNER):    
    """Mutates mask graphics, filling it with image provided."""
    w, h = mask.width, mask.height
    if mode == CORNER:
        xs, ys = int(x), int(y)
    else:
        xs, ys = int(x - w / 2), int(y - h / 2)
    img = create_image(w, h, ARGB)
    img.copy(img_fill, xs, ys, w, h, 0, 0, w, h)
    img.mask(mask)
    mask.begin_draw()
    mask.image(img, 0, 0)
    mask.end_draw()
    return mask

def speech_bubble(w, h):
    b = create_graphics(w, h)
    b.begin_draw()
    b.stroke_join(ROUND)
    b.stroke_weight(5) # note que no triângulo fica "meia espessura"
    b.triangle(w * 0.1, h / 2,
                  w / 2, h / 2,
                  w * 0.9, h * 0.9)             
    b.ellipse(w / 2, h / 2, w * 0.8, h * 0.8)
    b.no_stroke() # triangulo sem traço para "furar" a ellipse
    b.triangle(w * 0.1, h / 2,    # mata meia espessura, mas fica legal
                  w / 2, h / 2,
                  w * 0.9, h * 0.9)             
    b.end_draw()
    return b
