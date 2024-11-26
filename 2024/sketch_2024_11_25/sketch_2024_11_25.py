
def setup():
    size(700, 700)
    background(250, 250, 220)
    no_fill()
    colunas = filas = 10
    tamanho = width / colunas
    for j in range(filas): # i = 0, 1 ... filas-1
        y = j * tamanho + tamanho / 2
        for i in range(colunas): # i = 0, 1 ... colunas-1
            x = i * tamanho + tamanho / 2
            for _ in range(10):
                tq = random(tamanho / 10, tamanho - 2)
                stroke(random(128, 255),
                       random(255),
                       0)  
                ellipse(x, y, tq, tamanho - 2)
    save('out.png')

