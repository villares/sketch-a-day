from random import choice

caminhantes = []

def setup():
    size(600, 600) # tamanho da área de desenho
    background(255, 255, 100) # fundo amarelo
    for n in range(100):
        caminhantes.append((random(width),
                            random(height)))
        
def draw():
    noStroke()
    if frameCount < 500:
        for i, caminhante in enumerate(caminhantes):
            x, y = caminhante
            mx = random(-5, 5) # x = x + random(...)
            my = random(-5, 5)
            x += mx
            y += my
            fill(128 +  12 * mx + 12 * my) # fill(random(255), random(255), random(255))
            circle(x, y, random(5, 10))
            if x > width:   # largura da tela, 500
                x = x - width
            elif x < 0:
                x = width - x
            if y > height:   # altura da tela, 500
                y = y - height
            elif y < 0:
                y = height - y
            caminhantes[i] = (x, y)
            
def keyPressed():
    saveFrame('sketch_2021_02_27b.png')
