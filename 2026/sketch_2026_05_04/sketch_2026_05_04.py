GRID_N = 15

def setup():
    size(600, 600)
    text_align(CENTER, CENTER)
    no_fill()  # sem contorno
    stroke_weight(3)

def draw():
    background(127, 100, 127)  # fundo cinza claro
    f = remap(mouse_x, 0, width, 0, 1)
    base_spacing = int(width / (GRID_N + 0.01))
    v = remap(f, 1, 0, base_spacing * 1.5, base_spacing * sqrt(3))
    h = base_spacing * sqrt(3) #remap(f, 1, 0, base_spacing * sqrt(3), base_spacing * 2)
    for i in range(GRID_N):  # um i p/ cada coluna
        for j in range(GRID_N): # um j p/ cada linha
            if j % 2:
                x = i * h + (f * h / 4) 
            else:
                x = i * h - (f * h / 4)
            y = j * v
            n = 6 #8 - int(3 * f)
            poly(x, y, base_spacing, n, rot=f * radians(30))

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
    elif key == 's':
        save_frame('####.png')
