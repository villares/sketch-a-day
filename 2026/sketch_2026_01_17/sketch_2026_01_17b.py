def setup():
    size(1890, 450)
    fill(0)
    stroke(255)
    stroke_weight(1.5)
    
def draw():
    background(0)
    base = 20
    no_fill()
    w = base * 3
    h = base * 1.5
    for i in range(32):
        for j in range(16):
            if j % 2 == 0:
                x = i * w
            else:
                x = i * w + w / 2
            y = j * h
            grupo(x, y, base)    
    
def grupo(x, y, base):
    desc = base * 1.5
    pentagono(x, y, base, rot=False)
    pentagono(x, y, base, rot=False, flip=True)
    pentagono(x + desc, y, base, rot=True)
    pentagono(x - desc, y, base, rot=True, flip=True)

def pentagono(xb, yb, lado_base, rot=False, flip=False):
    t = remap(xb, 0, width, 0, 1)
    k = remap(t, 0, 1, -4, 2)
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
    save_frame('###-1890x450.png.png')
    