# Based on sketch 2020_10_28b

from villares.arcs import quarter_circle

N = 20

def setup():
    global w, variations, rotations
    size(900, 900)
    w = width / N
    # rectMode(CENTER)
    stroke_weight(2)
    stroke(255)
    no_fill()
    rotations = [0] * N * N
    variations = [
        random_choice([module0, module1, module2])
        for i in range(N * N)
    ]
    
def draw():
    background(0, 100, 100)
    for i in range(N):
        x = w / 2 + i * w
        for j in range(N):
            y = w / 2 + j * w
            push()
            translate(x, y)
            r = rotations[i + j * N]
            rotate(HALF_PI * r)
            module_func = variations[i + j * N]
            module_func(w)
            pop()

def module0(w):
    translate(-w / 2, -w / 2)
    stroke(0)
    if is_key_pressed and key_code == ALT:
        rect(0, 0, w, w)
    stroke(255)
    r = w / 2.0
    ri = w / 2.0
    q = w / 4.0
    d = w / 6.0
    line(r, 0, r, ri)
    line(ri, r, w, r)
    line(0, r, d, r)
    circle(d + d / 2.0, w / 2.0, d)
    line(r, r - q, 2.0 * q - d, r - q)
    circle(d + d / 2.0, w / 2.0 - q, d)
    line(r, w, r, w - d)
    circle(w / 2.0, w - (d + d / 2.0), d)

def module1(w): 
    translate(-w / 2.0, -w / 2.0)
    r = w / 2.
    line(0, r, r, 0)
    line(w, r, r, w)
    
def module2(w): 
    translate(-w / 2.0, -w / 2.0)
    r = w / 2.
    quarter_circle(0, 0, r, BOTTOM + RIGHT)
    quarter_circle(w, w, r, TOP + LEFT)
  
def key_pressed():
    if key == 's':
        save_frame('####.png')
    elif key == 'r':
        for i in range(N * N):
            rotations[i] = int(random(4))
    elif key == 'R':
        for i in range(N * N):
            rotations[i] = 0
    elif key == 'v':
        for i in range(N * N):
            variations[i] =  random_choice(
                [module0, module1, module2])
    elif key == 'V':
        for i in range(N * N):
            variations[i] = module0
