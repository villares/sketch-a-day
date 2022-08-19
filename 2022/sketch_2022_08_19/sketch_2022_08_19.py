from itertools import product
from villares.helpers import save_png_with_src

def setup():
    size(600, 600)
    rect_mode(CENTER)
    color_mode(HSB)
    no_stroke()
    w = 2
    for x, y in product(range(0, width + 1, w), repeat=2):
        if y % 10 < 5:
            fill(y % 250, 200, x % 200)
        else:
            fill(0)
        square(x, y, w)
    set_globals()

def set_globals():
    global x, y, w, h, x2, y2
    w, h = 100, 100
    x = random_int(0, (width - w) // 50) * 50
    y = random_int(0, (height - h) // 50) * 50
   
def draw():
    a = get(0, y, width - 1, h)
    b = get(width - 1, y, 1, h)
    image(a, 1, y)
    image(b, 0, y) 

    a = get(x, 0, w, height - 1)
    b = get(x, height - 1, w, 1)
    image(a, x, 1)
    image(b, x, 0) 

    if frame_count % 200 == 0:
        set_globals()

def key_pressed():
    if key == 's':
        save_png_with_src()