from random import shuffle
from collections import namedtuple

Ponto = namedtuple('Ponto', 'x y size, color')
pontos_ini, pontos_fim = [], []
a = 0  # animation control

add_library('VideoExport')

def setup():
    global videoExport
    size(400, 400)
    # background(0)
    colorMode(HSB)
    videoExport = VideoExport(this)
    videoExport.startMovie()
    
    ini = createGraphics(500, 500)
    ini.beginDraw()
    ini.textSize(100)
    ini.text("2019", 50, 250)
    ini.endDraw()
    pontos_ini[:] = set_points(ini, False)
    print(len(pontos_ini))

    fim = createGraphics(500, 500)
    fim.beginDraw()
    fim.textSize(100)
    fim.text("2020", 50, 250)
    fim.endDraw()
    pontos_fim[:] = set_points(fim, False)
    print(len(pontos_fim))
    
    background(0)

            
def draw():
    global a
    
    t = map(a, 0, 300, -1, 2)
    for p0, p1 in zip(pontos_ini, pontos_fim):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        # p_color = lerpColor(p0.color, p1.color, t)
        stroke(p0.color, 200)
        noFill()
        square(p_x, p_y, p_size)

    videoExport.saveFrame()

    if a < 100:
        a = lerp(a, 100.1, .05)
    elif a < 200:
        a = lerp(a, 200.1, .04)
    elif a < 300:
        a = lerp(a, 300.1, .5)
    else:
        a += 100    
        


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
    shuffle(pontos)
    return pontos

def keyPressed():        
    if key == 'q':
        videoExport.endMovie()
        exit()
