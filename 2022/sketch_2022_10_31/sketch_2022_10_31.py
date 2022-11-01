arrastando = None  # None quer dizer nenhum círculo sendo arrastado
circulos = []  # lista com coordenadas e tamanhos dos círculos
poly = []

def setup():
    size(400, 400)
    stroke_weight(3)
    fill(0, 200)  # preenchimento translúcido
    for _ in range(4):  # vamos sortear4 círculos
        d = 10
        x = random(d, width - d)
        y = random(d, height - d)
        circulos.append((x, y, d))
    poly[:] = circulos

def draw():
    background(0, 0, 200)
    no_fill()
    stroke(0)
    with begin_shape():
        for x, y, _ in poly:
            vertex(x, y)
    fill(0)
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        if i == arrastando:
            stroke(200, 0, 0)
        else:
            stroke(255)
        ellipse(x, y, d, d)


def mouse_pressed():  # quando um botão do mouse é apertado
    global arrastando
    # vamos olhar um círculo por vez da lista `circulos`
    for i, circulo in enumerate(circulos):  # i é o índice na lista
        x, y, d = circulo
        dist_mouse_circulo = dist(mouse_x, mouse_y, x, y)
        raio = d / 2
        if dist_mouse_circulo < raio:  # se o mouse estiver dentro
            arrastando = i
            break  # interrompe o laço, não checa mais outros!


def mouse_released():  # quando um botão do mouse é solto
    global arrastando
    arrastando = None
    poly[:] = circulos

def mouse_dragged():  # quando o mouse é movido apertado
    if arrastando is not None:
        x, y, d = circulos[arrastando]
        x += mouse_x - pmouse_x
        y += mouse_y - pmouse_y
        circulos[arrastando] = (x, y, d)


