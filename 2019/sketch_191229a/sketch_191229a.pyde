from random import shuffle
from collections import namedtuple
Ponto = namedtuple('Ponto', 'x y size, color')
pontos = []

def setup():
    global bg
    size(400, 400)
    background(0)
    colorMode(HSB)
    bg = createGraphics(500, 500)
    bg.beginDraw()
    bg.textSize(140)
    bg.text("Hello", 25, 250)
    bg.endDraw()
    set_points()
    
def set_points():
    step = 10
    i = 0
    for y in range(0, width, step):
        for x in range(0, width, step):
            bc = bg.get(x, y)
            if bc != 0:
                i = (i + 1) % 256
                c = color(i, 255, 255)
                pontos.append(Ponto(x, y, random(5, 10), c))
            else:
                c = 32
                # pontos.append(Ponto(x, y, random(5, 10), c))
    shuffle(pontos)
            
def draw():
    global a, v
    background(0)
    t = map(mouseX, 0, width, -1, 2)
    for p0, p1 in zip(pontos, pontos[::-1]):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        fill(p_color, 200)
        noStroke()
        circle(p_x, p_y, p_size)

def keyPressed():
    if key == ' ':
        background(0)
        pontos[:] = []
        set_points()
    if key == 's':
        saveFrame("i####.png")
