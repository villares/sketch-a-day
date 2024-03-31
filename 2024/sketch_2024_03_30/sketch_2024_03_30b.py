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

def setup():
    size(400, 300)

def draw():
    background(100)
    stroke_weight(3)
    stroke(0)
    no_fill()
    
    stroke_weight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        if i == arrastando:
            fill(200, 0, 0)
        elif dist(mouse_x, mouse_y, x, y) < 10:
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
        if dist(mouse_x, mouse_y, x, y) < 10:
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
        x += mouse_x - pmouse_x
        y += mouse_y - pmouse_y
        pontos[arrastando] = x, y

def key_pressed():
    save('out.png')