retangulos = []

def setup():
    size(600, 600) # área de desenho
    rectMode(CENTER)
    tamanho = 60
    for j in range(10):
        y = j * tamanho + tamanho / 2
        for i in range(10):
            x = i * tamanho + tamanho / 2
            for k in range(30):
                tam_sorteado = random(10, 60)
                cor = color(random(256), 100)
                # rect(x, y, tam_sorteado, tam_sorteado)
                retangulos.append((x, y, tam_sorteado, cor))
        
def draw():
    #background(200) # cor de fundo
    for x, y, tam, cor in reversed(retangulos):
        if dist(x, y, mouseX, mouseY) > tam / 2:
            fill(cor)
        else:
            fill(255, 0, 0, 100)
        rect(x, y, tam, tam)
            
