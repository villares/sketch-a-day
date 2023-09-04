def setup():
    global img
    size(800, 800)
    # https://pt.wikipedia.org/wiki/Ficheiro:Mappa_Topographico_do_Municipio_de_S%C3%A3o_Paulo_-_Folha_37,_Acervo_do_Museu_Paulista_da_USP.jpg
    img = load_image('/home/villares/GitHub/sketch-a-day/2023/sketch_2023_07_21/mapa.jpg')
    no_loop()
    image_mode(CENTER)
    
def draw():
    background(100)
    h = 50
    y = 7.5
    while y < height + h:
        w = 50
        x = 7.5
        while x < width + w:
            rm = g_balao_oval(w + 10, h + 10)
            clipped = fill_and_clip(
                rm, img,
                random(0, img.width - w),
                random(0, img.height - h))
            image(clipped, x + w / 2, y + h / 2)
            x += w + 7.5
            w *= 1.365
        y += h + 7.5
        h *= 1.365

    save_frame('####.png')
         
def fill_and_clip(mask, img_fill, x, y, mode=CORNER, draw_mask=False dst=None):    
    """Clip an image using a mask, filling it with image provided."""
    w, h = mask.width, mask.height
    dst = dst or create_graphics(w, h)
    if mode == CORNER:
        xs, ys = int(x), int(y)
    else:
        xs, ys = int(x - w / 2), int(y - h / 2)
    img = create_image(w, h, ARGB)
    img.copy(img_fill, xs, ys, w, h, 0, 0, w, h)
    img.mask(mask)
    dst.begin_draw()
    dst.image(img, 0, 0)
    dst.end_draw()
    return dst

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
