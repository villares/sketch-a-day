def setup():
    size(600, 600)
    f = loadFont("Inconsolata-Bold-48.vlw")
    textFont(f)
    desenho()
    saveFrame("desenho-sem-argumentos.png")
    
def desenho():
    noStroke()
    rect(0, 0, 300, 300) # fundo branco para o texto
    textAlign(CENTER, CENTER)
    fill(0) # preenchimento preto
    text("desenho()", 150, 150)
    rect(300, 0, 300, 300) # fundo preto para o olho
    olho(450, 150, 200)
    fill(100) # preenchimento cinza escuro
    rect(0, 300, 300, 300) # fundo para bandeirinha
    fill(255) # preenchimento branco
    stroke(0) # traço preto
    strokeWeight(15)
    bandeirinha(150, 450, 200)
    estrela(450, 450, 7, 100, 50)


def bandeirinha(x, y, tamanho):
    """ Bandeirinha na posição x, y com largura e altura 'tamanho' """
    metade = tamanho / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    beginShape()  # começa a desenhar a forma, inicia um polígono
    vertex(-metade, -metade)
    vertex(-metade, metade)
    vertex(0, 0)
    vertex(metade, metade)
    vertex(metade, -metade)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
    
def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela com np pontas
    raio a e raio b são os raios internos e das pontas
    """
    n = num_pontas * 2 # a forma é um polígono o dobro de pontos que as pontas
    inc = radians(360. / n) # ângulo de eincremento entre os pontos
    beginShape() # começa a desenhar a forma
    ang = 0 # começando com o ângulo 0
    while ang < TWO_PI:
        x = x_centro + sin(ang) * raio_a
        y = y_centro + cos(ang) * raio_a
        vertex(x, y)
        ang += inc
        x = x_centro + sin(ang) * raio_b
        y = y_centro + cos(ang) * raio_b
        vertex(x, y)
        ang += inc
    endShape(CLOSE) # encerra uma forma fechada
    
    
def olho(x, y, largura, cor=color(100)):
    """ Olho na posição x, y com largura e cor """
    pushStyle() # preserva os atributos gráficos atuais
    noStroke()
    fill(255)
    ellipse(x, y, largura, largura * .5)
    fill(cor)
    circle(x, y, largura * .4)
    fill(0)
    circle(x, y, largura * .1)
    popStyle() # retorna os atributos gráficos anteriores
