colunas = 50
filas = 50

def setup():  
    size(600, 600)

def draw():
    background(0)
    no_stroke()
    cw = width / colunas # largura celula/coluna (também altura da fila)
    for i in range(colunas):
        x = i * cw + cw / 2
        for j in range(filas):
            y = j * cw + cw / 2
            # diâmeto baseado na distância do centro
            d = (dist(x, y, width/2, height/2) / 5) % cw
            # cinza baseado no produto da linha e coluna
            v = ((i+1) * (j+1) * 5) % 255
            fill(v)
            # desenho do elemento em x, y
            circle(x, y, d)

def key_pressed():
    save_frame('out.png')