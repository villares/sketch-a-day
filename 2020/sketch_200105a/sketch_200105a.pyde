from random import shuffle
from collections import namedtuple

Ponto = namedtuple('Ponto', 'x y size')
pontos_ini, pontos_fim = [], []
a = 0  # animation control

def setup():
    global videoExport, ini, fim
    size(400, 400)
    colorMode(HSB)
       
    ini = draw_text('SP', 200, 250, text_size=140)
    pontos_ini[:] = set_points(ini, shuffle_points=True)
    print(len(pontos_ini))
    
    fim = draw_text('PCD', 200, 100,text_size=100)    
    pontos_fim[:] = set_points(fim, shuffle_points=True)
    print(len(pontos_fim))
    
def draw_text(txt, x, y, text_size=120): 
    img = createGraphics(width, height)
    img.beginDraw()
    img.textAlign(CENTER, CENTER)
    img.textSize(text_size)
    img.text(txt, x, y)
    img.endDraw()
    return img
                    
            
def draw():
    global a
    background(100)
    for a in range(0, 256, 10):    
        t = map(a, 0, 256, -.2, 1.2)
        for p0, p1 in zip(pontos_ini, pontos_fim):
            p_x, p_y = lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t)
            p_size = lerp(p0.size, p1.size, t)
            stroke(a, 255, 255, 100)
            noFill()
            square(p_x, p_y, p_size)
         


def set_points(p_graphics, bg_points=False,  shuffle_points=True):
    pontos = []
    step = 4
    i = 0
    for y in range(0, width, step):
        for x in range(0, width, step):
            bc = p_graphics.get(x, y)
            if bc != 0:
                pontos.append(Ponto(x, y, random(5, 10)))
            else:
                if bg_points:
                    pontos.append(Ponto(x, y, random(1, 5)))
    if  shuffle_points:
        shuffle(pontos)
    return pontos

def keyPressed():        
    if key == 's':
        saveFrame("s####.png")
