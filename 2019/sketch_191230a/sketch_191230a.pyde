add_library('VideoExport')
from random import shuffle
from collections import namedtuple
Ponto = namedtuple('Ponto', 'x y size, color')
pontos = []
pontos_draw = []

def setup():
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()
    global bg
    size(400, 400)
    background(0)
    colorMode(HSB)
    bg = createGraphics(500, 500)
    bg.beginDraw()
    bg.textSize(140)
    bg.text("adeus", 2, 190)
    bg.text("2019", 25, 308)
    bg.endDraw()
    set_points()

def set_points():
    step = 7
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
    # shuffle(pontos)

def draw():
    global a, v
    background(0)
    l = len(pontos_draw)
    t = map(l, 0, len(pontos), -1, 0)
    for p0, p1 in zip(pontos_draw, pontos_draw[::-1]):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        fill(p_color, 200)
        noStroke()
        circle(p_x, p_y, p_size)

    videoExport.startMovie()

    for _ in range(4):
            l = len(pontos_draw)
            if l < len(pontos):
                pontos_draw.append(pontos[l])

def keyPressed():
    if key == 'n':
        background(0)
        pontos[:] = []
        pontos_draw[:] = []
        set_points()
    if key == 's':
        saveFrame("i####.png")

    
    if key == 'q':
        videoExport.endMovie()
