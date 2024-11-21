# Sketch usando py5 "imported mode", precisa do Thonny + plugin ou sketch runner

formas = []

def setup():
    global pos_atual, direcao
    size(600, 600)
    background(0) # fundo preto
    no_stroke()
    color_mode(HSB) # Matiz, Sat, Brilho
    
    pos_atual = Py5Vector(0, 0) # v.x, v.y
    apontar_direcao(0)
    largura_octogono = 200
    lado_octogono = largura_octogono / (1 + sqrt(2))
    
    translate(-largura_octogono / 2, -largura_octogono / 2)
    
    andar(lado_octogono / sqrt(2))
    #pontos_octogono = []
    for i in range(8): # fazer 8 vezes:
        andar(lado_octogono)
        girar(360 / 8)
        #pontos_octogono.append(pos_atual)
        triangulo_e_quadrado(lado_octogono)
    # desenhar estrela central
    # deslocada meio octogono pra baixo e pra direita
    ladinho = lado_octogono / (2 + sqrt(2)) # lado quadradinho
    girar(90)
    andar(largura_octogono - ladinho * sqrt(2) / 2)
    girar(-90)
    andar(largura_octogono / 2)
    andar(ladinho)
    pontos_estrela = []  # lista vazia
    for i in range(16):
        if i % 2 == 0:  # se i é par:
            girar(-90)
        else:  # senão:
            girar(90 + 45)
        andar(ladinho)
        pontos_estrela.append(pos_atual)
        #circle(pos_atual.x, pos_atual.y, 10)
    formas.append(pontos_estrela)

    for i in range(4): # 0, 1, 2, 3
        x = i * largura_octogono
        for j in range(4): # 0, 1, 2, 3
            y = j * largura_octogono
            desenha_todas_as_formas(x, y)

    save(__file__[:-3] + '.png')
  
def quadradinho(lado):
    pontos_quadradinho = []
    for i in range(4):  # repita 4 vezes:
        andar(lado)
        girar(90)
        pontos_quadradinho.append(pos_atual)
    formas.append(pontos_quadradinho)
  
def triangulo_e_quadrado(lado_octogono):
    ladinho = lado_octogono / (2 + sqrt(2)) # lado quadradinho
    pontos_triangulo = [pos_atual]
    girar(45)
    andar(lado_octogono / sqrt(2))
    pontos_triangulo.append(pos_atual)
    #circle(pos_atual.x, pos_atual.y, 10)
    quadradinho(ladinho) 
    girar(-90)
    andar(lado_octogono / sqrt(2))
    pontos_triangulo.append(pos_atual)
    girar (-90-45)
    #andar(lado_octogono)
    andar(ladinho)
    pontos_triangulo.append(pos_atual)
    #circle(pos_atual.x, pos_atual.y, 10)
    girar(-45)
    andar(ladinho)
    pontos_triangulo.append(pos_atual)
    girar(90)
    andar(ladinho)
    #circle(pos_atual.x, pos_atual.y, 10)
    pontos_triangulo.append(pos_atual)
    girar(-45)
    #circle(pos_atual.x, pos_atual.y, 10)
    pontos_triangulo.append(pos_atual)
    andar(ladinho)
    # fim do lado com dente
    girar(180)
    formas.append(pontos_triangulo)
  
def andar(d):
    global pos_atual
    pos_atual = pos_atual + Py5Vector.from_heading(direcao) * d

def apontar_direcao(deg):
    global direcao
    direcao = radians(deg)

def girar(deg):
    global direcao
    direcao += radians(deg)

def desenha_todas_as_formas(x, y):
    with push_matrix():
        translate(x, y)
        for i, shp in enumerate(formas):
            fill(128 + i // 8 * 15, 255, 200)
            desenha_forma(shp)

def desenha_forma(pts):
    with begin_closed_shape():
        vertices(pts)
