from random import shuffle
from collections import namedtuple

Ponto = namedtuple('Ponto', 'x y size, color')
pontos_end, pontos_ini = [], []
a = 0  # animation control

def setup():
    size(600, 400)
    color_mode(HSB)
    f = create_font('Courier', 70)
    img = create_graphics(600, 400)
    img.begin_draw()
    img.text_font(f)
    img.text_size(70)
    img.text("Processing", 30, 100)
    img.text("+ Python?", 30, 200)
    img.text("meet py5!", 30, 300)
    img.end_draw()
    pontos_end[:] = set_points(img)
    print(len(pontos_end))
    img.begin_draw()
    img.clear()
    img.text_font(f)
    img.text_size(70)
    img.text("São Paulo", 30, 150)
    img.text("& Ciberlândia", 30, 250)
    img.end_draw()
    pontos_ini[:] = set_points(img)
    print(len(pontos_ini))            
            
def draw():
    global a
    background(0)
    t = remap(a, 0, 300, -1, 2)
    for p0, p1 in zip(pontos_ini, pontos_end):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerp_color(p0.color, p1.color, t)
        fill(p_color, 100)
        # stroke(p0.color, 200)
        no_stroke()
        square(p_x, p_y, p_size)

    if a < 100:
        a = lerp(a, 101, 0.02)
    elif a < 200:
        a = lerp(a, 200.1, 0.02)
    elif a < 300:
        a = lerp(a, 300.1, 0.4)
    else:
        a += 5            
    if a > 800:
        a = 0
        exit_sketch()
    save_frame('####.png')


def set_points(p_graphics, bg_points=False,  shuffle_points=True):
    pontos = []
    step = 3
    i = 0
    for y in range(0, width, step):
        for x in range(0, width, step):
            bc = p_graphics.get_pixels(x, y)
            if bc != 0:
                i = (i + 0.1) % 256
                c = color(i, 200, 200)
                pontos.append(Ponto(x, y, random(3, 18), c))
            else:
                if bg_points:
                    c = color(128, 100)
                    pontos.append(Ponto(x, y, random(2, 17), c))
    if  shuffle_points:
        shuffle(pontos)
    return pontos

def key_pressed():        
    if key == 's':
        save_frame("s####.png")
