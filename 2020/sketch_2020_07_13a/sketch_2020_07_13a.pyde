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
            seta_vetor(x, y, r)

def seta_vetor(xo, yo, v):
    """Desenhe uma seta na posição xo, yo usando o vetor v."""
    body = v.mag()
    ang = v.heading()
    head_size = max(5, body / 5)
    xh = xo + cos(ang) * body
    yh = yo + sin(ang) * body
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    push()  # preserva os atributos gráficos atuais
    fill(g.strokeColor)  # usa a cor de traço como preenchimento!
    noStroke()
    beginShape()
    xha = xh + cos(ang + QUARTER_PI / 2 + PI) * head_size
    yha = yh + sin(ang + QUARTER_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - QUARTER_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - QUARTER_PI / 2 + PI) * head_size
    vertex(xha, yha)  
    vertex(xh, yh)
    vertex(xhb, yhb)
    endShape(CLOSE)
    pop()  # devolve os atributos ao que eram antes
