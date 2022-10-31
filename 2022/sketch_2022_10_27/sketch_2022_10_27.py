from itertools import combinations, permutations

rnd = 1

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
    
    
def draw():
    random_seed(rnd)
    s = 0.02
    background(0)
    for cor_a, cor_b in permuts:
        x = random(width)
        step = random_int(5, 10) * 2
        for y in range(0, height, step):
            fill(cor_a)
            ellipse(x + 10 * os_noise((y + 2 * frame_count) * s, x * s),
                    y + step / 2, step / 2, step / 2)
        step = random_int(5, 10) * 2
        for y in range(0, height, step):
            fill(cor_b) 
            ellipse(x + 10 * os_noise((y + 2 * frame_count) * s, x * s),
                    y, step / 2, step / 2)

def key_pressed():
    global rnd
    if key == ' ':
        rnd += 1
    elif key == 's':
        save_frame('###.png')