from itertools import combinations, permutations

def setup():
    global permuts
    size(700, 700)
    color_mode(HSB) # Hue (Matiz), Sat, Bri
    rect_mode(CENTER)
    no_stroke()
    cores = []
    for i in range(8):
        cor = color(32 + i * 24, 255 - i * 16, 128 + i * 16)
        cores.append(cor)

    permuts = list(permutations(cores, 2))
    print(len(permuts))
    no_loop()
    no_smooth()
    
def draw():
    background(0)
    x = 18
    for cor_a, cor_b in permuts:
        step = random_int(1, 3) * 10
        for y in range(2, height - 5, step):
            fill(cor_a)
            rect(x, y + 5, step, 4)
        step = random_int(1, 3) * 10
        for y in range(2, height - 5, step):
            fill(cor_b)
            rect(x, y, step, 4)
        x += 12
        
def key_pressed():
    if key == ' ':
        redraw()
    elif key == 's':
        save_frame('###.png')