from random import choice

def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    strokeJoin(ROUND)
    blendMode(MULTIPLY)

def draw():
    background(255)
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
    noFill()
    strokeWeight(3)
    stroke(64 + i * 64, 64 + j * 64, 200)
    """ Seta na posição x, y com largura w e altura h"""
    mw = w 
    mh = h 
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    r = choice((0, 1, 2, 4))
    rotate(r * HALF_PI)
    beginShape()  # começa a desenhar a forma, inicia um polígono
    a, b = random_pair(s / 5)
    vertex(a, b - mw)
    a, b = random_pair(s / 5)
    vertex(a - mw  , b)
    a, b = random_pair(s / 5)
    vertex(a - mw, b + mh)
    a, b = random_pair(s / 5)
    vertex(a, b + mh - mw)
    a, b = random_pair(s / 5)
    vertex(a + mw, b + mh)
    a, b = random_pair(s / 5)
    vertex(a + mw, b)
    # vertex(0, 0)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
     
def random_pair(r):
    return random(-r, r), random(-r, r) 

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
