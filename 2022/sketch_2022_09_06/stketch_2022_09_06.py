from itertools import product

def setup():
    global x, y, w, th
    size(200, 520)
    translate(40, 20)
    no_stroke()
    rect_mode(CENTER)
    w = 30
    th = w * sqrt(3) / 2    
    x = y = w
    
    
    combos = list(product(
         ((t, True), (t, False)),
         ((s, True), (s, False)),
         ((c, True), (c, False))
        ))
    print(f'Combinations: {len(combos)}')
    
    for combo in combos:
        for func, state in combo:
            func(state)
            x += w
        x += w
        if x > width - 5 * w:
            x = w
            y += 2 * w

def t(on):
    fill(255 * on)
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def s(on):
    fill(255 * on)
    square(x, y, w * 0.85),
   
def c(on):
    fill(255 * on)
    circle(x, y, w)
