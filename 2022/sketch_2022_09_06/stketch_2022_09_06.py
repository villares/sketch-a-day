from itertools import product

w = 30  # width base-value for single element
th = w * sqrt(3) / 2  # triangle height

def setup():
    size(180, 520)
    no_stroke()
    rect_mode(CENTER)

    shapes = (t, s, c)  # triangle, square, circle
    on_offs = (((shp, True), (shp, False)) for shp in shapes)
    combos = list(product(*on_offs))
    print(f'Combinations: {len(combos)}')

    translate(w, w / 2)
    x = y = w
    for combo in combos:
        for func, state in combo:
            draw_element(state * 255, func, x, y)
            x += w
        x += w
        if x > width - 5 * w:
            x = w
            y += 2 * w

def draw_element(c, shape_func, x, y):
    fill(c)
    shape_func(x, y)

def t(x, y):
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def s(x, y):
    square(x, y, w * 0.85),
   
def c(x, y):
    circle(x, y, w)
