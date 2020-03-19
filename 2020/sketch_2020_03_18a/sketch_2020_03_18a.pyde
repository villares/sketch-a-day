def setup():
    """ executa no começo """
    size(500, 500) # tamanho do desenho
    # não vamos usar cores RGB, vamos usar HSB
    colorMode(HSB) # Matiz, Saturação e Brilho
    noStroke() # sem contorno nas formas
    
def draw():    
    """ 
    tudo que executa repetidas vezes
    (isso permite animações e interação)
    """
    background(100) # fundo e limpeza da tela cinza
    tam = mouseX / 20.
    espaco = 1 + mouseY / 20. # o 1 é pra não ter divisão por zero
    linhas, colunas = int(height / espaco), int(width / espaco)
    for j in range(linhas):
        y = espaco / 2 + j * espaco
        for i in range(colunas):
            x = espaco / 2 + i * espaco
            ang = radians(x / 2. + y / 2. + frameCount)
            matiz = 128 + 128 * sin(ang)
            cor = color(matiz, 255, 255)
            fill(cor)
            ellipse(x, y, tam, tam)
    
def keyPressed():
    if key == 's':
        saveFrame('image###.png')
