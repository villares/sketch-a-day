from collections import namedtuple
Ponto = namedtuple('Ponto', 'x y size, color')
a, v, pontos = 0, 1, []

def setup():
    size(500, 500)
    colorMode(HSB)
    noFill()
    noStroke()

def draw():
    global a, v
    background(0)
    t = map(a, 0, 100, 0, 1)
    for p0, p1 in zip(pontos, pontos[::-1]):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        fill(p_color)
        circle(p_x, p_y, p_size)

    if a > 0:
        a += v
    if a > 300:
        v = -v

def mouseDragged():
    c = color(len(pontos) % 256, 255, 255, 150)
    pontos.append(Ponto(mouseX, mouseY, random(5, 15), c))

def keyPressed():
    global a, v
    if key == 'a':
        a, v = 1, 1
    if key == ' ':
        background(0)
        pontos[:] = []
