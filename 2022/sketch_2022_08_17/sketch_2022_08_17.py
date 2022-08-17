from itertools import product
from villares.helpers import save_png_with_src

def setup():
    size(600, 600)
    rect_mode(CENTER)
    color_mode(HSB)
    no_stroke()
    for x, y in product(range(0, width + 1, 20), repeat=2):
        fill(y % 255, x % 200, 200)
        square(x, y, 20)
    set_globals()

def set_globals():
    global x, y, w, h, x2, y2
    w, h = random_int(5, 10) * 10, random_int(5, 10) * 10
    x = random_int(0, (width - w) // 10) * 10
    y = random_int(0, (height - h) // 10) * 10
   
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