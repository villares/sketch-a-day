from random import choice

def setup():
    size(700, 700)
    rectMode(CENTER)
    strokeJoin(ROUND)
    noLoop()

def draw():
    background(0)
    noFill()
    g = list(grid(700, 20, 700, 20))
    # println(g)
    for _ in range(20):
        x, y = choice(g)
        stroke(x / 3, y / 3, 255)
        circle(x, y, 10)
        poly_arrow(width / 2, width / 2, x, y)

def grid(w, cols, h, rows):
    cw = w / cols
    rh = h / rows
    for x in range(cw / 2, w, cw):
        for y in range(rh / 2, h , rh):
            yield x, y

def poly_arrow(x, y, w, h):
    """ Seta na posição x, y com largura w e altura h"""
    mw = w / 2
    mh = h / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    beginShape()  # começa a desenhar a forma, inicia um polígono
    vertex(0, -0 - mw)
    vertex(-mw  , 0)
    vertex(-mw, mh)
    vertex(0, mh - mw)
    vertex(mw, mh)
    vertex(mw, 0)
    # vertex(0, 0)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
    

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
