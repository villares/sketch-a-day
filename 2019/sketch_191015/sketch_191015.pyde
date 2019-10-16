from random import choice
from elementos import casinha, estrela, olho, grade

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
            o = choice((0, 1, 2))
            if e is not None: # faz elemento de uma grade de elementos iguais
                element(x, y, cw, e)
            elif cw > 40 and random(10) < 8: # faz subdivisão recursiva
                poster(x, y, 3, cw) 
            elif cw > 20 and random(10) < 8:  # faz grade de elementos iguais
                poster(x, y, 3, cw * 2, o + 3)
            else:  # faz um elemento "sozinho"
                element(x, y, cw, o)
    if xo == width / 2.: # uma vez só, para a grade-poster grande apenas
        # define tamanho e sorteia posicão no quadrante esquerdo inferior
        w_olho = width / 16 # tamanho do olho
        x_olho, y_olho = random(w_olho, width / 2), random(height / 2, height - w_olho)
        fill(0)
        square(x_olho, y_olho, w_olho + 2)
        olho(x_olho, y_olho, w_olho)


def element(x, y, w, option, single=False):
    stroke(0)
    strokeWeight(1)
    if option == 0:
        fill(0)
        num_pontas = choice((3, 5, 7))
        ra, rb = w / 3, choice((w/6, w*.1, w*.2))
        estrela(x, y, num_pontas, ra, rb)
    elif option == 1:
        fill(255, 0, 0)
        casinha(x, y, w)
    elif option == 2:
        fill(255, 0, 255)
        casinha(x, y, w)
    elif option == 3:
        noFill()
        casinha(x, y, w)
    elif option == 4:
        noFill()
        casinha(x, y, w)        



def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
