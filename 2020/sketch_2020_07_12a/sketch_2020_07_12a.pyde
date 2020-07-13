from __future__ import division

points = [PVector(150, 150), PVector(300, 300), None]

def setup():
    global s, n
    size(600, 600)
    noCursor()  # desativa a setinha do mouse
    s = 15
    n = int(width / s)
    
def draw():
    background(200)
    points[2] = PVector(mouseX, mouseY)
    for i in range(n):
        x = s / 2 + i * s
        for j in range(n):
            y = s / 2 + j * s
            r = PVector()
            for p in points:
                d = dist(x, y, p.x, p.y)
                g = PVector(x, y)
                v = (p - g)
                v.normalize()
                v *= 1000 / (1 + d)
                v.limit(s * 2)
                r += v 
            vetor(x, y, r)

def vetor(xa, ya, v):
    # xb, yb = v.x, v.y
    tam = v.mag()
    ang = v.heading()
    tam_ponta = tam / 5 * sqrt(2)
    xp = xa + cos(ang) * tam
    yp = ya + sin(ang) * tam
    line(xa, ya, xp, yp)  # corpo com tamanho fixo
    xpe = xp + cos(ang + QUARTER_PI/2 + PI) * tam_ponta
    ype = yp + sin(ang + QUARTER_PI/2 + PI) * tam_ponta
    line(xp, yp, xpe, ype)  # parte esquerda da ponta
    xpd = xp + cos(ang - QUARTER_PI/2 + PI) * tam_ponta
    ypd = yp + sin(ang - QUARTER_PI/2 + PI) * tam_ponta
    line(xp, yp, xpd, ypd)  # parte direita da ponta
