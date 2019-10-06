from random import choice

def setup():
    size(700, 700)
    rectMode(CENTER)
    strokeJoin(ROUND)
    noLoop()

def draw():
    background(0)
    noFill()
    # c, r = 11 + int(10 * sin(frameCount/5.)), 11 + int(10 * cos(frameCount/5.))
    # print(c, r)
    g = list(grid(600, 20, 600, 20))
    for _ in range(50):
        x, y = choice(g)
        stroke(x / 3, y / 3, 255)
        poly_arrow(width / 2, width / 2, x, y)



def grid(w, cols, h, rows):
    cw = w / cols
    rh = h / rows
    for x in range(cw / 2, w + cw, cw):
        for y in range(rh / 2, h + rh, rh):
            yield x, y

def poly_arrow(x, y, w, h):
    """ Casinha na posição x, y com largura e altura 'tamanho' """
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
