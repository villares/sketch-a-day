from random import shuffle
from collections import namedtuple

Ponto = namedtuple('Ponto', 'x y size, color')
pontos_ini, pontos_fim = [], []

def setup():
    global bg
    size(400, 400)
    background(0)
    colorMode(HSB)
    
    ini = createGraphics(500, 500)
    ini.beginDraw()
    ini.textSize(138)
    ini.text("2019", 28, 250)
    ini.endDraw()
    pontos_ini[:] = set_points(ini, False)

    fim = createGraphics(500, 500)
    fim.beginDraw()
    fim.textSize(134)
    fim.text("2020", 18, 250)
    fim.endDraw()
    pontos_fim[:] = set_points(fim, False)
    
def set_points(p_graphics, bg_points=True):
    pontos = []
    step = 7
    i = 0
    for y in range(0, width, step):
        for x in range(0, width, step):
            bc = p_graphics.get(x, y)
            if bc != 0:
                i = (i + 1) % 256
                c = color(i, 255, 255)
                pontos.append(Ponto(x, y, random(5, 10), c))
            else:
                if bg_points:
                    c = 32
                    pontos.append(Ponto(x, y, random(5, 10), c))
    # shuffle(pontos)
    return pontos
            
def draw():
    global a, v
    background(0)
    t = map(mouseX, 0, width, -1, 2)
    for p0, p1 in zip(pontos_ini, pontos_fim):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        fill(p_color, 200)
        noStroke()
        circle(p_x, p_y, p_size)

def keyPressed():
    if key == 's':
        saveFrame("i####.png")
