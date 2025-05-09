def setup():
    size(450, 450)
    
def draw():
    base = 75
    no_fill()
    w = base * 3
    h = base * 1.5
    for i in range(3):
        for j in range(5):
            if j % 2 == 0:
                x = i * w
            else:
                x = i * w + w / 2
            y = j * h
            grupo(x, y, base)    
    
def grupo(x, y, base):
    desc = base * 1.5
    fill(150, 0, 0)
    pentagono(x, y, base, rot=False)
    fill(250, 50, 50)
    pentagono(x, y, base, rot=False, flip=True)
    fill(0, 0, 150)
    pentagono(x + desc, y, base, rot=True)
    fill(50, 50, 250)
    pentagono(x - desc, y, base, rot=True, flip=True)

def pentagono(xb, yb, lado_base, rot=False, flip=False):
    k = remap(mouse_x, 0, width, -4, 2)
    vs = [
        (-2 + k,  0),
        (-3, -3),
        ( 0, -4 - k),
        ( 3, -3),
        ( 2 - k,  0)
    ]
    u = lado_base / 4
    with begin_closed_shape():
        for i, j in vs:
            if flip:
                j = -j
            if rot:
               i, j = j, -i
            x = xb + i * u
            y = yb + j * u
            vertex(x, y)
    
def key_pressed():
    save_frame('###.png')
    