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
    combos = list(product((wt,bt), (ws, bs), (wc, bc)))
    print(f'Combinations: {len(combos)}')
    for combo in combos:
        for s in combo:
            s()
            x += w
        x += w
        if x > width - 5 * w:
            x = w
            y += 2 * w

def wt():
    fill(255)
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def ws():
    fill(255)
    square(x, y, w * 0.85),
   
def wc():
    fill(255)
    circle(x, y, w)

def bt():
    fill(0)
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def bs():
    fill(0)
    square(x, y, w * 0.85),
   
def bc():
    fill(0)
    circle(x, y, w)
