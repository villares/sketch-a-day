from random import shuffle
from collections import namedtuple
add_library('VideoExport')

Ponto = namedtuple('Ponto', 'x y size, color')
pontos_ini, pontos_fim = [], []
a = 0  # animation control

def setup():
    global videoExport
    size(400, 400)
    colorMode(HSB)
    
    ini = createGraphics(500, 500)
    ini.beginDraw()
    ini.textSize(60)
    ini.text("Processing", 10, 150)
    ini.text("Community", 10, 250)
    ini.text("Day SP 2020", 10, 350)

    ini.endDraw()
    pontos_ini[:] = set_points(ini, bg_points=False,  shuffle_points=True)
    print(len(pontos_ini))

    fim = createGraphics(500, 500)
    fim.beginDraw()
    fim.textSize(70)
    fim.text(u"Obrigado!", 10, 150)
    fim.text("#PCD20SP", 10, 250)
    fim.endDraw()
    pontos_fim[:] = set_points(fim, bg_points=False, shuffle_points=True)
    print(len(pontos_fim))
    videoExport = VideoExport(this)
    videoExport.startMovie()    
    background(0)
            
            
def draw():
    global a
    # background(0)
        
    t = map(a, 0, 300, -1, 2)
    for p0, p1 in zip(pontos_ini, pontos_fim):
        p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        fill((a * 2) % 255, 255, 255, 100)
        # stroke(p0.color, 200)
        # noFill()
        square(p_x, p_y, p_size)

    if a < 100:
        a = lerp(a, 100.1, .05)
    elif a < 200:
        a = lerp(a, 200.1, .04)
    elif a < 300:
        a = lerp(a, 300.1, .8)
    else:
        a += 05            
    videoExport.saveFrame()

def set_points(p_graphics, bg_points=True,  shuffle_points=True):
    pontos = []
    step = 4
    i = 0
    for y in range(0, width, step):
        for x in range(0, width, step):
            bc = p_graphics.get(x, y)
            if bc != 0:
                # i = (i + 1) % 256
                c = color(random(128, 255))
                pontos.append(Ponto(x, y, random(3, 8), c))
            else:
                if bg_points:
                    c = color(128, 100)
                    pontos.append(Ponto(x, y, random(2, 7), c))
    if  shuffle_points:
        shuffle(pontos)
    return pontos

def keyPressed():        
    if key == 's':
        saveFrame("s####.png")
    if key == 'q':
        videoExport.endMovie()
        exit()
