# -*- encoding: utf-8 -*-

def casinha(x, y, tamanho):
    """ Casinha na posição x, y com largura e altura 'tamanho' """
    metade = tamanho / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    beginShape()  # começa a desenhar a forma, inicia um polígono
    vertex(0, -metade)
    vertex(-metade, 0)
    vertex(-metade, metade)
    vertex(metade, metade)
    vertex(metade, 0)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
    
def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela com np pontas
    raio a e raio b são os raios internos e das pontas
    """
    n = num_pontas * 2 # dobro de pontos que as pontas
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
    ellipse(x, y, largura, largura * .45)
    fill(cor)
    circle(x, y, largura * .4)
    fill(0)
    circle(x, y, largura * .1)
    popStyle() # retorna os atributos gráficos anteriores
    
    
def grade(xo, yo, n, tam_total):
    tam_celula = tam_total / n
    desloc = (tam_celula - tam_total) / 2.
    for i in range(n):
        x = xo + desloc + tam_celula * i
        for j in range(n):
            y =  yo + desloc + tam_celula * j
            rectMode(CENTER)
            square(x, y, tam_celula * .6)
