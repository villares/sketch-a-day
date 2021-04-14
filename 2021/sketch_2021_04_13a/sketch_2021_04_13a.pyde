from __future__ import division

def setup():
    size(1000, 1000)
    background(200)
    strokeWeight(0.1)
    grade(0, 0, width, 5)
    saveFrame("sketch_2021_04_13a.png")
    
def grade(xo, yo, largura_total, ordem):
    colunas = filas = ordem
    largura_celula = largura_total / colunas
    for i in range(colunas):
        x = xo + i * largura_celula
        for j in range(filas):
            y = yo + j * largura_celula
            fill(i * 64, j * 64, 128)
            if largura_celula > 4 and random(10) > 5:
                 grade(x, y, largura_celula, 5)
            else:
                rect(x, y, largura_celula, largura_celula)
        
