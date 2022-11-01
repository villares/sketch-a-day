from itertools import combinations, permutations

s = 0.05
rnd = 1

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
    
def draw():
    random_seed(rnd)
    background(0)
    x = 18
    for cor_a, cor_b in permuts:
        step = random_int(1, 3) * 5
        for y in range(2, height - 5, step):
            fill(cor_a)
            xo = step / 2 * os_noise(x, (y + 5 + frame_count) * s)  
            ellipse(x + xo, y + 5, step / 2, step / 2)
        step = random_int(1, 3) * 5
        for y in range(2, height - 5, step):
            fill(cor_b)
            xo = step / 2 * os_noise(x, (y + 5 + frame_count) * s)  
            ellipse(x + xo, y, step / 2, step / 2)
        x += 12
        
def key_pressed():
    if key == ' ':
        global rnd
        rnd += 1
    elif key == 's':
        save_frame('###.png')