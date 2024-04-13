# Foto do Lobo:
# https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/
# Mexican_Wolf_2_yfb-edit_1.jpg/640px-Mexican_Wolf_2_yfb-edit_1.jpg

import py5

def setup():
    global img, out
    py5.size(800, 533)
    out = py5.create_graphics(py5.width, py5.height)
    img = py5.load_image('lobo.jpg')
    py5.no_loop()
    
def draw():
    py5.background(0)
    n = 6
    for i in range(n):
        out.begin_draw()
        iw, ow = img.width // n, img.width // n
        out.copy(img, i * iw, 0, iw, img.height, i * ow, 0, ow, img.height)
        out.apply_filter(py5.POSTERIZE, 2 + i)
        out.end_draw()
    out.load_np_pixels()
    out.np_pixels.sort()
    out.update_np_pixels()
    for _ in range(5):
        py5.image(out, 0, 0)

def key_pressed():
    py5.save(f'out.jpg')
    
py5.run_sketch(block=False)