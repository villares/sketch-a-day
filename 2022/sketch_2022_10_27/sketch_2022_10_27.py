from itertools import combinations, permutations
from itertools import combinations_with_replacement
from itertools import product

def setup():
    global permuts
    size(800, 800)
    color_mode(HSB) # Hue (Matiz), Sat, Bri
    no_stroke()
    cores = []
    for i in range(8):
        cor = color(32 + i * 24, 255 - i * 16, 128 + i * 16)
        cores.append(cor)

    permuts = list(permutations(cores, 2))
    print(len(permuts))
    no_loop()
    
def draw():
    background(0)
    for cor_a, cor_b in permuts:
        x = random(width)
        step = random_int(5, 10) * 2
        for y in range(0, height, step):
            fill(cor_a)
            rect(x, y, step, 5)
        step = random_int(5, 10) * 2
        for y in range(0, height, step):
            fill(cor_b)
            rect(x, y, step, 5)

def key_pressed():
    if key == ' ':
        redraw()
    elif key == 's':
        save_frame('###.png')