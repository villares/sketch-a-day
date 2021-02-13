from random import choice

points = [] 

def setup():
    global bgd, linhas
    size(564, 750, P3D)
    textAlign(CENTER)
    textMode(SHAPE)
    fonte = createFont("Tomorrow Bold",12)
    textFont(fonte)
    linhas = sumario.split('\n')    
    bgd = choice(colors)
    points[:] = choose_points()
    
def choose_points():
    points = []
    points.append(PVector.random3D() * 128)
    while len(points) < len(linhas):
        p = PVector.random3D() * 128
        if 127 < PVector.dist(p, points[-1]) < 128:
            points.append(p)
    return points
    
def draw():
    background(bgd)
    strokeWeight(5)
    translate(width / 2, height / 2, 128)
    scale(-1)
    rotateY(mouseX / 100.0)
    for i, (xa, ya, za) in enumerate(points):
        xb, yb, zb = points[i - 1]
        # fill(128 + xa, 128 + ya, 128 + za)
        fill(colors[i % len(colors)])
        text_line(linhas[i], xa, ya, za, xb, yb, zb)

        
def keyPressed():
    global bgd
    if key == 's':
        saveFrame("######.png")
    elif key == ' ':
        bgd = choice(colors)
    elif key == 'w':
        bgd = color(240)

                                
colors = (color(250, 50, 0),
          color(150, 0, 0),
          color(250, 0, 0),
          color(0, 150, 0),
          color(50, 50, 250),
          color(0, 50, 150),
          color(150, 50, 250),
          color(50, 150, 250)
          )

sumario = u"""
Meu amigo Max Brod
As cólicas de Michel de Montaigne 
Que rei sou eu? 
O futuro de uma ilusão 
Do ateísmo geográfico 
Pais e filhos 
Sociedade dos Ateus Anônimos 
Baseado em fatos reais 
A coisa pública 
Do aborto ao botox 
Magia negra A bola parada 
Como vieram ao mundo  
Suspeitei desde o princípio 
Pra não dizer que não falei dos beagles 
Não seja você mesmo, por favor 
Profissão não é mérito 
O sétimo dia Nazi baby 
Sísifo on the beach 
Condenar o pecado, perdoar a literatura do pecador 
Democracia: modos de usar 
Milagres que se repetem
Toda nudez será ignorada
A cultura brasileira (não) existe
Da medicina como corte e costura
Escravos de Jó
No pictures
Crime sem castigo
Que argumento, afinal de contas, é um par de tetas?
O cru e o cozido
Mula sem cabeça
Ao infinito e além
O verdadeiro desporto nacional
Pôneis malditos
O último bípede
O taxista metafísico
Risco de vida
Onde vivem os monstros
Ler não é crime
A identidade na época de sua reprodutibilidade técnica
Teatro mágico
Preço não é valor
Capeletti gay
Caminho suave
Esse tal de espírito olímpico
Uma nota de rodapé ao golpe de 
Reler é preciso, ler não é preciso
Toda forma de amor
Educação sentimental
Eu, leitor
Esta cidade não merece um verso
Vida\rde artista
O fator Hitler
Capitalistas, graças a Deus
O doente imaginário
É isto um livro? 
Síndrome de Estocolmo 
Em briga de mulher e mulher, homem não mete a colher 
A natureza não é mãe; é madrasta 
Je suis quem, exatamente?
Meu mel, não diga adeus 
A vida secreta dos livros 
Memento mori
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
        
