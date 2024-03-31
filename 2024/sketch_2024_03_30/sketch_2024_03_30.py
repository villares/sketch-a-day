arrastando = None

pontos = [
    (100, 50),   # 0: vertex inicial
    (150, 100),  # 1: ponto de controle
    (250, 100),  # 2: vértice-âncora
    (250, 200),  # 3: ponto de controle
    (150, 200),  # 4: vértice-âncora
    (50, 200),   # 5: ponto de controle
    (50, 100),   # 6: vértice-âncora
]

s = 2 # scale factor

def setup():
    size(800, 600)

def draw():
    scale(s)
    background(100)
    stroke_weight(3)
    stroke(0)
    no_fill()

    with begin_shape():
        vertex(pontos[0][0], pontos[0][1])
        for (px, py), (x, y) in zip(pontos[1::2], pontos[2::2]):
            quadratic_vertex(px, py, x, y)
    
    stroke_weight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        if i == arrastando:
            fill(200, 0, 0)
        elif dist(mouse_x / s, mouse_y / s, x, y) < 10:
            fill(255, 255, 0)
        else:
            fill(255)
        ellipse(x, y, 5, 5)
        t = f'{i}: {"vertex" if i == 0 else "control" if i % 2 else "quadratic"}'
        text(t, x + 5, y - 5)


def mouse_pressed():
    global arrastando
    for i, ponto in enumerate(pontos):
        x, y = ponto
        if dist(mouse_x / s, mouse_y / s, x, y) < 10:
            arrastando = i
            break 

def mouse_released():
    global arrastando
    arrastando = None

def mouse_dragged():
    global pontos
    global arrastando
    if arrastando is not None:
        x, y = pontos[arrastando]
        x += (mouse_x - pmouse_x) / s
        y += (mouse_y - pmouse_y) / s
        pontos[arrastando] = x, y

def key_pressed():
    save('out.png')