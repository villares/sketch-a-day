from random import choice

caminhantes = []

def setup():
    size(600, 600) # tamanho da área de desenho
    background(255, 255, 100) # fundo amarelo
    for n in range(100):
        caminhantes.append((random(width),
                            random(height)))
        
def draw():
    stroke(random(255)) # fill(random(255), random(255), random(255))
    if frameCount < 500:
        for i, caminhante in enumerate(caminhantes):
            x, y = caminhante
            x0, y0 = caminhante
            # circle(x, y, 2)
            x += choice((-5, 0, 5)) # x = x + random(...)
            y += choice((-5, 0, 5))
            line(x0, y0, x, y)
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
    saveFrame('sketch_2021_02_27a')
