
def setup():
    size(800, 800)
    no_loop()
    
def draw():

    background(240, 240, 255)
    # https://pt.wikipedia.org/wiki/Ficheiro:Mappa_Topographico_do_Municipio_de_S%C3%A3o_Paulo_-_Folha_37,_Acervo_do_Museu_Paulista_da_USP.jpg
    img = load_image('/home/villares/GitHub/sketch-a-day/2023/sketch_2023_07_21/mapa.jpg')
    h = 50
    y = 7.5
    while y < height + h:
        w = 50
        x = 7.5
        while x < width + w:
            rm = rect_mask(w, h)
            clipped = fill_and_clip(
                rm, img,
                random(0, img.width - w),
                random(0, img.height - h))
            image(clipped, x, y)
            x += w + 7.5
            w *= 1.365
        y += h + 7.5
        h *= 1.365

    save_frame('####.png')
         
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

def rect_mask(w, h, sw=4):
    b = create_graphics(int(w), int(h))
    b.begin_draw()
    b.stroke_join(ROUND)
    b.stroke_weight(sw) 
    b.rect(sw / 2, sw / 2, w - sw, h - sw)
    b.end_draw()
    return b

def key_pressed():
    redraw()