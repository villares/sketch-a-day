colunas = 10
filas = 10

def setup():  
    size(400, 400)
    color_mode(HSB)

def draw():
    background(0)
    no_stroke()
    cw = width / colunas # largura celula/coluna (também altura da fila)
    for i in range(colunas):
        x = i * cw + cw / 2
        for j in range(filas):
            y = j * cw + cw / 2
            # diâmeto baseado na soma da linha  coluna
            d = 10 + cw * (i + j) / (colunas * 2.5)
            # matiz baseado no produto da linha e coluna
            h = 10 + (i * j) * 2.2
            c = color(h, 255, 200)
            fill(c)
            # desenho do elemento em x, y
            circle(x, y, d)

def key_pressed():
    save_frame('out.png')