"""
"Based on traditional Japanese stitching,
this is a riff on hitomezashi patterns." Annie Perikins @anniek_p
https://twitter.com/anniek_p/status/1244220881347502080?s=20
"""
from random import choice

tam = 10
mtm = tam / 2  # meio tamanho
grid = dict()

def setup():
    global cols, rows
    size(400, 400)
    cols, rows = width / mtm - 1, height / tam

def init():
    for y in range(rows):
        on = choice((True, False))
        for x in range(cols):
            if x % 2 == 1:
                if x % 4:
                    on = not on
                grid[(x, y)] = on
    for x in range(cols):
        on = choice((True, False))
        for y in range(rows):
            if x % 2 == 0:
                on = not on
                grid[(x, y)] = on

def ngbs(x, y):
    nbs = []
    if x % 2 == 0:
        nb_list = ((-1, 0), (-1, 1), (1, 0), (1, 1))
    else:     
        nb_list = ((-1, 0), (-1, -1), (1, 0), (1, -1))
    for nx, ny in nb_list:
        nb = x + nx, y + ny
        if grid.get(nb, 'no') != 'no':
            nbs.append.(nb)
            
def draw():
    background(200)
    noLoop()
    init()

    for i in range(cols):
        x = i * mtm + mtm
        for j in range(rows):
            y = j * tam + mtm
            nbs = ngbs(i, j)
            if dist(x, y, mouseX, mouseY) < tam:
                for n in nbs:
                    ni, nj = n
                    nx =  ni * mtm + mtm
                    ny =  nj * tam + mtm
                    circle(nx, ny, 4)
                    
            
            if grid[(i, j)]:
                if i % 2 == 0:
                    line(x, y - mtm, x, y + mtm)
                else:
                    line(x - mtm, y - mtm, x + mtm, y - mtm)


def mouseReleased():
    loop()
    saveFrame("####.png")
