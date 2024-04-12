# Foto do Lobo: Carlos Delgado
# https://commons.wikimedia.org/wiki/File:Canis_lupus_signatus_-_01.jpg

import py5

def setup():
    global img, out
    py5.size(640 * 2, 384 * 2)
    
    img = py5.load_image('lupus.jpg')
    n = 8
    for i in range(n):
        out = py5.create_graphics(py5.width, py5.height)
        out.begin_draw()
        iw, ow = img.width // n, out.width // n
        out.copy(img, i * iw, 0, iw, img.height, i * ow, 0, ow, out.height)
        out.apply_filter(py5.POSTERIZE, 2 + i)
        out.end_draw()
        py5.image(out, 0, 0)

def key_pressed():
    py5.save(f'out.jpg')
    
py5.run_sketch(block=False)