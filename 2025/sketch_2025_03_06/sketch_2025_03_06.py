import py5

CT = """Collage from "Mercado Municipal (São Paulo)" by Wilfredo Rafael Rodriguez Hernandez (Wilfredor)
https://commons.wikimedia.org/wiki/File:Mercado_Municipal_(S%C3%A3o_Paulo)_16.jpg
Creative Commons Attribution-Share Alike 4.0 International license.
"""


def setup():
    global img
    py5.size(800, 640)
    img = py5.load_image('Mercado_Municipal_(São_Paulo)_16.jpg')
    py5.no_loop()
    py5.image_mode(py5.CENTER)
    
def draw():
    py5.no_loop()
    py5.background(0)
    w = h = 200
    py5.stroke_weight(15)
    mask = make_mask(w + 10, h + 10)
    #image(img, 300, 300, img.width / 2, img.height / 2)
    
    for x in range(50, py5.width, 100):
        for y in range(50, py5.height, 100):
            clipped = clip_with_mask(
                    img, mask,
                    py5.random(0, img.width - w),
                    py5.random(0, img.height - h))
            py5.image(clipped, x, y, 100, 100)
    py5.fill(255)
    py5.text(CT, 20, py5.height - 30)
    py5.save_frame('####.png')
         
def make_mask(w, h):
    m = py5.create_graphics(int(w), int(h))
    m.begin_draw()
    m.fill(255)
    m.circle(w / 2, h / 2, w - 10)
    m.end_draw()
    return m
         
def clip_with_mask(img, mask, x, y):    
    """Clip an image using a mask, its dimensions, and a position."""
    w, h = mask.width, mask.height
    result = py5.create_image(mask.width, mask.height, py5.ARGB)
    result.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    result.mask(mask)
    return result

def key_pressed():
    py5.redraw()

py5.run_sketch(block=False)
