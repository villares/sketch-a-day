from random import choice

def setup():
    size(600, 600)
    noLoop()
    # strokeJoin(ROUND)
    blendMode(MULTIPLY)
    colorMode(HSB)
    rectMode(CENTER)

def draw():
    global c
    c = 220
    background(255)
    grid(width / 2, width / 2, 4, width)

def grid(xo, yo, n, tw, e=None):
    global c
    # c += 1
    """
    Faça o desenho do grid baseado em uma subdivisão (grade) recursiva
    """
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            if cw > 20 and random(10) < 8: # faz subdivisão recursiva
                grid(x, y, 3, cw) 
            else:  # faz um elemento "sozinho"
                fill(c)
                rect(x, y, cw * 2, cw * 2, i * 5, j * 5, i * 5, j * 5)





def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
