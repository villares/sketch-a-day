from collections import namedtuple

Ponto = namedtuple('Ponto', 'x y size, color')
pontos = []

def setup():
    size(500, 500)
    colorMode(HSB)
    noFill()

def draw():
    background(0)
    if keyPressed:
        t = map(frameCount % 100, 0, 99, 0, 1)
    else:
        t = 0
        
    for p0, p1 in zip(pontos, pontos[::-1]):
        p_x = lerp(p0.x, p1.x, t)
        p_y = lerp(p0.y, p1.y, t)
        p_size = lerp(p0.size, p1.size, t)
        p_color = lerpColor(p0.color, p1.color, t)
        stroke(p_color)
        circle(p_x, p_y, p_size)

def mouseDragged():
    c = color(len(pontos) % 256, 255, 255)
    pontos.append(Ponto(mouseX, mouseY, random(5, 25), c))

def keyPressed():
    if key == ' ':
        pontos[:] = []
    
