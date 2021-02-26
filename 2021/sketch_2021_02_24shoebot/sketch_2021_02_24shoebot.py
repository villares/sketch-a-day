from math import *
from nodebox.geo import distance

PI = pi
QUARTER_PI = pi / 4

def setup():
    size(400, 400)
    speed(60)
    
def draw():
    background(200)
    stroke(0)
    for i in range(10):
        x = 20 + i * 40
        for j in range(10):
            y = 20 + j * 40
            if distance(x, y, MOUSEX, MOUSEY) > 35:
                seta_tam_fixo(x, y, MOUSEX, MOUSEY, 35)  
    
def seta_tam_fixo(xa, ya, xb, yb, tam):
    ang = atan2(yb - ya, xb - xa)
    tam_ponta = tam / 4 * sqrt(2)
    xp = xa + cos(ang) * tam
    yp = ya + sin(ang) * tam
    line(xa, ya, xp, yp)  # corpo com tamanho fixo
    xpe = xp + cos(ang + QUARTER_PI + PI) * tam_ponta
    ype = yp + sin(ang + QUARTER_PI + PI) * tam_ponta
    line(xp, yp, xpe, ype)  # parte esquerda da ponta
    xpd = xp + cos(ang - QUARTER_PI + PI) * tam_ponta
    ypd = yp + sin(ang - QUARTER_PI + PI) * tam_ponta
    line(xp, yp, xpd, ypd)  # parte direita da ponta
