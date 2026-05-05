GRID_N = 15
rnd_seed = 1

def setup():
    size(600, 600)
    text_align(CENTER, CENTER)
    no_fill()  # sem contorno
    stroke_weight(3)

def draw():
    background(127, 100, 127)  # fundo cinza claro
    random_seed(rnd_seed)
    f = remap(mouse_x, 0, width, 0, 1)

    base_spacing = int(width / (GRID_N + 0.01))

    v = remap(f, 1, 0, base_spacing * 1.5, base_spacing * sqrt(3))
    h = base_spacing * sqrt(3) #remap(f, 1, 0, base_spacing * sqrt(3), base_spacing * 2)
    for _ in range(1):
        for ix in range(GRID_N):  # um x p/ cada coluna
            # um y p/ cada linha
            for iy in range(GRID_N):
                if iy % 2:
                    x = ix * h + (f * h / 4) 
                else:
                    x = ix * h - (f * h / 4)
                y = iy * v
                n = 6 #8 - int(3 * f)
                r = remap(f, 0, 1, 0, radians(30))
                poly(x, y, base_spacing, n, r)

def poly(x, y, r, n=6, rot=0):
    with push_matrix():
        translate(x, y)
        rotate(rot)  # radians(30) for "pointy", 0 for "flat" hexagon
        with begin_closed_shape():
            for i in range(n):
                sx = cos(i * TWO_PI / n) * r
                sy = sin(i * TWO_PI / n) * r
                vertex(sx, sy)

def key_pressed():
    global rs
    if key == ' ':
        rs += 1
    elif key == 's':
        save_frame('####.png')
