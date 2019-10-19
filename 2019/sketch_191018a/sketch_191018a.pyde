from random import choice

def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(100)
    grid(width / 2, width / 2, 4, width)

def grid(xo, yo, n, tw, e=None):
    """
    Faça o desenho do grid baseado em uma subdivisão (grade) recursiva
    """
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            if cw > 30 and random(10) < 8: # faz subdivisão recursiva
                grid(x, y, 3, cw) 
            else:  # faz um elemento "sozinho"
                poly_arrow(x, y, cw, i, j)



def poly_arrow(x, y, s, i, j):
    w = s / (1 + i) # x / s)
    h = s / (1 + j ) # y / s)
    """ Seta na posição x, y com largura w e altura h"""
    mw = w 
    mh = h 
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    r = choice((0, 1, 2, 4))
    rotate(r * HALF_PI)
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
