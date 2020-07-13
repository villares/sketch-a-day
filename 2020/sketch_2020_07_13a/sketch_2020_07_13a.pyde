from __future__ import division

points = [PVector(150, 150), PVector(300, 300), None]

def setup():
    global s, n
    size(500, 500)
    # colorMode(HSB)
    noCursor()  # desativa a setinha do mouse
    s = 10
    n = int(width / s)
    # strokeWeight(1.5)

def draw():
    # background(0)
    background(240, 240, 200)
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
                if (p.x, p.y) == (mouseX, mouseY):
                    v *= -1
                v.normalize()
                v *= 1000 / (1 + d)
                v.limit(s * 2)
                r += v
            # c = map(r.heading(), -PI, PI, 0, 255)
            # stroke(c, 255, 255)
            vetor(x, y, r)

def vetor(xa, ya, v):
    # xb, yb = v.x, v.y
    push()
    tam = v.mag()
    ang = v.heading()
    tam_ponta = max(5, tam / 5)
    xp = xa + cos(ang) * tam
    yp = ya + sin(ang) * tam
    line(xa, ya, xp, yp)  # corpo com tamanho fixo
    fill(g.strokeColor)  # gets current stroke!
    noStroke()
    beginShape()
    xpe = xp + cos(ang + QUARTER_PI / 2 + PI) * tam_ponta
    ype = yp + sin(ang + QUARTER_PI / 2 + PI) * tam_ponta
    xpd = xp + cos(ang - QUARTER_PI / 2 + PI) * tam_ponta
    ypd = yp + sin(ang - QUARTER_PI / 2 + PI) * tam_ponta
    vertex(xpe, ype)  # parte esquerda da ponta
    vertex(xp, yp)
    vertex(xpd, ypd)  # parte direita da ponta
    endShape(CLOSE)
    pop()
