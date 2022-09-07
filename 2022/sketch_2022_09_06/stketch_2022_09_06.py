from itertools import product

w = 30
th = w * sqrt(3) / 2    

def setup():
    size(180, 520)
    no_stroke()
    rect_mode(CENTER)

    shapes = (t, s, c)  # triangle, square, circle
    on_offs = (((shp, True), (shp, False)) for shp in shapes)
    combos = list(product(*on_offs))
    print(f'Combinations: {len(combos)}')
    x = y = w
    translate(w, w / 2)
    for combo in combos:
        for func, state in combo:
            draw_shp(state * 255, func, x, y)
            x += w
        x += w
        if x > width - 5 * w:
            x = w
            y += 2 * w

def draw_shp(c, shp, x, y):
    fill(c)
    shp(x, y)

def t(x, y):
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def s(x, y):
    square(x, y, w * 0.85),
   
def c(x, y):
    circle(x, y, w)
