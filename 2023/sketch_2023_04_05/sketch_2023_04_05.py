from random import choice 

paleta = [
    color(100, 0, 0), color(0, 100, 0), color(0, 0, 100),
    color(0), color(255), color(100, 100, 0)
]

def setup():
    size(800, 800)
    background(240, 240, 220)
    no_fill()
    n = 15 # filas e colunas
    lado = width / n
    for i in range(n):
        x = lado / 2 + i * lado
        for j in range(n):
            y = lado / 2 + j * lado
            # x, y, lado máximo, bagunça, repetições
            quadrado_molnar(x, y, lado, lado / 30, 10)  

def quadrado_molnar(x, y, lado, faixa_bagunca, repete):
    for k in range(repete):
        w = random(5, lado)   # tamanho randomizado
        x0, y0 = x - w / 2, y - w / 2
        x1, y1 = x + w / 2, y - w / 2
        x2, y2 = x + w / 2, y + w / 2
        x3, y3 = x - w / 2, y + w / 2
        stroke(choice(paleta))
        begin_shape()
        for xv, yv in ((x0, y0), (x1, y1), (x2, y2), (x3, y3)):                   
            bx = random(-faixa_bagunca, faixa_bagunca)
            by = random(-faixa_bagunca, faixa_bagunca)
            vertex(xv + bx, yv + by)
        end_shape(CLOSE)
        
        