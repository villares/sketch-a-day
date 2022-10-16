

def setup():
    size(800, 800)
    background(200)
    no_fill()
    no_loop()
    random_seed(1)

def draw():
    background(200)
    x = y = width / 2
    poligonos_recursivos(x, y, width / 4)

def poligonos_recursivos(xo, yo, r, n=6):
    a = TWO_PI / n
    pontos = [(xo + r * cos(i * a), yo + r * sin(i * a))  
              for i in range(n)]
    sorteio = random_choice((True, False))
    w = width
    if r > w / 10 or (sorteio and r > w / 200):
        for x, y in pontos:
            stroke_weight(r / 50)
            line(x, y, xo, yo)
            poligonos_recursivos(x, y, r / 2, n)
    else:
        stroke_weight(r / 10)
        with begin_closed_shape():
            vertices(pontos)

def key_pressed(e):
    save_frame('imagem.png')
    redraw()

