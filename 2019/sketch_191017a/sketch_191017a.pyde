from random import choice

def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(255)
    poster(width / 2, width / 2, 4, width)

def poster(xo, yo, n, tw, e=None):
    """
    Faça o desenho do poster baseado em uma subdivisão (grade) recursiva
    """
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            elif cw > 30 and random(10) < 8: # faz subdivisão recursiva
                poster(x, y, 3, cw) 
            else:  # faz um elemento "sozinho"
                element(x, y, cw)



def poly_arrow(x, y, s):
    w = s / (1 + x / s)
    h = s / (1 + y / s)
    """ Seta na posição x, y com largura w e altura h"""
    mw = w / 2
    mh = h / 2
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
