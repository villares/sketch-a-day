import random, pickle

points = [] 


random.seed(3)    

def setup():
    global bgd, linhas
    size(750, 750, P3D)
    textAlign(CENTER)
    textMode(SHAPE)
    fonte = createFont("Tomorrow Bold",18)
    textFont(fonte)
    linhas = sumario.split('\n')    
    bgd = random.choice(colors)
    points[:] = choose_points()
    

    
def choose_points():
    points = []
    # points.append(tuple(PVector.random2D() * 128))
    for i in range(len(linhas) * 5 ):
        r = width / 6
        p = PVector((i * 20) % height, (i % 60) * 50) 
        # if r - 30 < PVector.dist(p, PVector(*points[-1])) < r + 30:
        points.append((p.x, p.y, i % 2 * 50))
    return points
    
def draw():
    background(240)
    # background(255, 229, 0)
    strokeWeight(5)
    translate(width / 4, height , 128)
    scale(-1)
    rotateY(mouseX / 100.0)
    for i, (xa, ya, za) in enumerate(points):
        xb, yb, zb = points[i - 1]
        fill(128 + xa, 128 + ya, 128 + za)
        fill(colors[i % len(colors)])
        # fill(0)
        text_line(linhas[i % len(linhas)], xa, ya, za, xb, yb, zb) #i * 10) #,zb)

        
def keyPressed():
    global points
    global bgd
    if key == 's':
        saveFrame("######.png")
    elif key == 'd':
        with open("data/positions.pickle", "wb") as file:
            pickle.dump(points, file)
    elif key == 'l':
        with open("data/positions.pickle", "rb") as file:
            points = pickle.load(file)
                

                                
colors = (color(250, 50, 0),
          color(150, 0, 0),
          color(250, 0, 0),
          # color(0, 150, 0),
          # color(50, 50, 250),
          # color(0, 50, 150),
          color(150, 50, 250),
          # color(50, 150, 250)
          )

sumario = u"""
 Geraldo Filme (1927–1995) já foi Negrinho das Marmitas, Geraldão da Barra Funda e
 Tio Gê, entre tantas outras alcunhas que marcaram o percurso desse sambista
 excepcional. Foi, antes de tudo, símbolo de resistência. Combateu obstinadamente
 três duros processos de apagamento: o do samba, perseguido pela polícia; o da
 negritude, desvalorizada em seu protagonismo; 
 e o da memória da cidade de São Paulo, esquecida na acelerada urbanização.

A vocação para resistir aparece cedo, aos 10 anos, quando o menino Geraldo decide
 provar ao pai que existe samba de verdade na capital da garoa. E produz a prova
 da maneira mais prática e poética possível: compõe o samba “Eu vou mostrar”. A
 partir de então, o samba negro paulista se faria presente e persistente em suas
 composições.

Ouvir Geraldo Filme é transportar-se para o tempo do samba batido com latão de
 lixo e caixa de engraxate no extinto Largo da Banana, na Barra Funda.
 São cenários vivamente construídos onde enxerga-se o drama dos negros, diplomados
 apenas na escola de samba, eternamente oprimidos em suas manifestações culturais,
 como o jogo de tiririca e o batuque de Pirapora do Bom Jesus. E Tio Gê não ficava
 só na superfície do que via ou do que já tinha vivenciado. Como um verdadeiro
 pesquisador, vasculhou os arquivos da cidade para resgatar Tebas, negro
 escravizado e ás da alvenaria, responsável pela construção das torres da Catedral da Sé.

O novo lançamento do Selo, Tio Gê – O samba paulista de Geraldo Filme, traz toda a
 genialidade e a coerência da obra do artista, com um repertório organizado de
 maneira a mostrar ao público o desenvolvimento da carreira do sambista. O projeto,
 idealizado por Fernando Cardoso, traz 20 composições de Geraldo Filme,
 interpretadas por cantoras negras de diferentes gerações. Somam-se a elas textos
 do escritor Léo Lama sobre a vida de Tio Gê, interpretados pelos atores Aílton
 Graça, Sidney Santiago Kuanza e João Acaiabe, que podem ser conferidos na íntegra
 (abaixo) acompanhados das 20 faixas do álbum (já disponível nas plataformas
 digitais) na sequência.
"""      

def text_line(txt, x1, y1, z1, x2, y2, z2,
                  y_offset=4, truncate=False):
    """Draw a box rotated in 3D like a text_line/edge."""
    stroke(0, 0, 200)
    # line(x1, y1, z1, x2, y2, z2)
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    # box(weight, weight, p1.dist(p2))
    rotateY(HALF_PI)
    if screenY(0, 0, 0) - screenY(0, 6, 0) > 0: rotateX(PI)
    if screenX(0, 0, 0) - screenX(6, 0, 0) > 0: rotateY(PI)
    if truncate:
        text(truncate_text(txt, p1.dist(p2)), 0, y_offset)
    else:
        text(txt, 0, y_offset)
    popMatrix()
    
    
    
def truncate_text(txt, tw):
    w = 0
    p = 0
    while w < tw and p < len(txt):
        p += 1
        w = textWidth(txt[:p])
    return txt[:p] 
        
