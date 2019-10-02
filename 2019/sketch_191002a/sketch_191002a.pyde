from random import choice
from elementos import olho, casinha, grade_s, estrela

def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    noStroke()

def draw():
    background(255)
    grade(300, 300, 3, 600.)

def grade(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = (i + j) % 4
            if e is not None:
                element(x, y, cw, e)
            elif cw > 50 and random(10) < 5:
                grade(x, y, 3, cw)
            elif cw > 50:
                fill(255)
                grade(x, y, 3, cw, o)
            else:
                fill(0)
                noStroke()
                element(x, y, cw, o)

def element(x, y, w, option):
    if option == 0:
        noStroke()  # desliga o traço
        fill(0)  # preenchimento preto
        rect(x, y, w, w)  # fundo
        olho(x, y, w / 2, 200)
    else:
        # fill(255) # preenchimento branco
        stroke(0)  # traço preto
        strokeWeight(w / 20)  # espessura do traço
        # if option == 1 and w > 50:
        # fill(100) # preenchimento cinza escuro
        #     noStroke()
        # rect(x, y, w, w) # fundo
        #     fill(255)
        #     grade(x, y, 1, w)
        if option == 1:
            fill(100)
            casinha(x, y, w / 2)
        else:
            radius_pairs = choice(((w / 3, w / 4),
                                   (w / 5, w / 4),
                                   (w / 5, w / 3),
                                   ))
            estrela(x, y, choice((5, 7, 9, 11)), *radius_pairs)


def keyPressed():
    saveFrame("####.png")
    redraw()
