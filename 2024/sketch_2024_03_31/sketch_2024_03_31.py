arrastando = None

pontos = [
    (100, 50),   # 0: vertex ponto âncora inicial 
    (150, 150),  # 1: primeiro ponto de controle
    (250, 150),  # 2: segundo ponto de controle
    (200, 200),  # 3: vértice bezier
    (150, 250),  # 4: primeiro ponto de controle
    (50, 200),   # 5: segundo ponto de controle
    (50, 100),   # 6: vértice bezier
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

    begin_shape()
    for i, (x, y) in enumerate(pontos):
        if i == 0:
            vertex(x, y)
        elif i % 3 == 0:  # elementos divisíveis por 3 da lista
            c1x, c1y = pontos[i - 2]
            c2x, c2y = pontos[i - 1]
            bezier_vertex(c1x, c1y,  #  primeiro ponto de controle
                          c2x, c2y,  #  segundo ponto de controle
                          x, y),     #  vértice
    end_shape()
    
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
        t = f'{i}: {"vertex" if i == 0 else f"control-{i%3}" if i % 3 else "bezier"}'
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