d = 400
n = 11
s = 3

def setup():
    size(600, 600)
    
def draw():
    background(230, 190, 190)  # R G B
    #estrela(300, 300, d, db, n, rot=radians(frame_count * 0.2)) # x, y, d, db, n
    estrela_cruzando(300, 300, d, n, s)
    
def estrela_cruzando(x, y, d, n, skip, rot=0):
    r = d / 2
    pontos = []
    passo = TWO_PI / n
    for i in range(n): # i=0, 1, 2... n-1
        xv = x + r * cos(i * passo + rot)
        yv = y + r * sin(i * passo + rot)
        pontos.append((xv, yv))
    i = None
    no_fill()
    stroke_weight(10)
    begin_shape()
    while i != 0:
        if i is None:
            i = 0
        vertex(*pontos[i])
        i = (i + skip) % n
    end_shape(CLOSE)
    fill(255)
    text_size(40)
    text(f'{n=} {s=}', 20, 40)
            
def key_pressed():
    global n, s
    if key == 'a':
        n += 1
    elif key == 'z':
        n -= 1
    elif key == 's':
        s += 1
    elif key == 'x':
        s -= 1
    

def mouse_wheel(evento):
    global d
    c = evento.get_count()
    d = d + c * 5
       


