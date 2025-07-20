# Based on sketch 2020_10_28b

from villares.arcs import quarter_circle

N = 15

def setup():
    global w, d, variations, rotations
    size(909, 909)
    w = width / N
    d = w / 6
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
    background(0, 128, 100)
#     translate(500, 500)
#     scale(4)
#     module0(w)
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
    if is_key_pressed and key_code == ALT:
        stroke(0, 0, 255)
        rect(0, 0, w, w)
    stroke(255)
    r = w / 2
    dc = w / 8
    #stroke(0)
    quarter_circle(0, 0, r - d, BOTTOM + RIGHT)
    quarter_circle(0, 0, r + d, BOTTOM + RIGHT)
    quarter_circle(w, w, r - d, TOP + LEFT)
    quarter_circle(w, w, r + d, TOP + LEFT)
    stroke(255)
    line(r, 0, r, r)
    line(r, r, w, r)  
    line(0, r, dc, r)
    circle(dc + dc / 2, w / 2, dc)    
    line(r, w, r, w - dc)
    circle(w / 2, w - (dc + dc / 2), dc)
    # stroke(0, 0, 200) for debug
    line(d + dc + dc / 2, r - d, r, r - d,)
    circle(d + dc, r - d, dc)


def module1(w): 
    translate(-w / 2, -w / 2)
    r = w / 2
    stroke(255)
    line(0, r, r, 0)
    line(w, r, r, w)
    #stroke(0)
    line(0, r - d, r - d, 0)
    line(w, r - d, r - d, w)
    line(0, r + d, r + d, 0)
    line(w, r + d, r + d, w)


def module2(w): 
    translate(-w / 2, -w / 2)
    r = w / 2
    stroke(255)
    quarter_circle(0, 0, r, BOTTOM + RIGHT)
    quarter_circle(w, w, r, TOP + LEFT)
    #stroke(0)
    quarter_circle(0, 0, r - d, BOTTOM + RIGHT)
    quarter_circle(0, 0, r + d, BOTTOM + RIGHT)
    quarter_circle(w, w, r - d, TOP + LEFT)
    quarter_circle(w, w, r + d, TOP + LEFT)

def key_pressed():
    if key == 's':
        save_frame('####.png')
    elif key == 'r':
        for i in range(N * N):
            rotations[i] = int(random(4))
    elif key == 'R':
        for i in range(N * N):
            if variations[i] != module0:
                rotations[i] = 0
    elif key == 'v':
        for i in range(N * N):
            variations[i] =  random_choice(
                [module0, module1, module2])        
            
    elif key == 'V':
        for i in range(N * N):
            variations[i] = module2
