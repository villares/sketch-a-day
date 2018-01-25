"""
s18020b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Slider code by Peter Farell (older version tweeked by me)
https://github.com/hackingmath/python-sliders
"""
#from slider import Slider

# r1 = Slider(-50, 50, 0)
# r2 = Slider(-50, 50, 0)
# np = Slider(3, 50, 10)

CEL_SIZE = 50
HALF_CEL = CEL_SIZE / 2

pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

TAM_PONTO = 50  # TAM_PONTO dos Pontos \
TAM_BARRA = 100
VEL_MAX = 2  # velocidade máxima nas ortogonais vx e vy


def setup():
    global ROWS, COLS  # filas e colunas
    size(400, 400)
    fill(0)
    ROWS, COLS = int(height / CEL_SIZE), int(width / CEL_SIZE)
    for r in range(ROWS):
        for c in range(COLS):
            x, y = HALF_CEL + c * CEL_SIZE,\
                   HALF_CEL + r * CEL_SIZE
            pontos.add(Ponto(x, y))  # acrescenta um Ponto



import random as rnd  # para não conflitar com o random do Processing


def draw():
    background(128)        # limpa a tela
    # para cada ponto
    for ponto in pontos:
        ponto.desenha()  # desenha
        ponto.move()    # atualiza posição
    # para cada aresta
    for aresta in arestas:  # checa se há Arestas com Pontos já removidos
        if (aresta.p1 not in pontos) or (aresta.p2 not in pontos):
            arestas.remove(aresta)   # nesse caso remove a Aresta também
        else:                # senão
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra()  # altera a velocidade dos pontos

# Sob clique do mouse seleciona/deseleciona Pontos ou Arestas
def mouseClicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção
    mouse = PVector(mouseX, mouseY)
    for aresta in arestas:    # para cada Aresta checa o 'mouse over'
        if pointInsideLine(mouse, aresta.p1, aresta.p2, 6):
            aresta.sel = not aresta.sel  # inverte status de seleção


def keyPressed():   # Quando uma tecla é pressionada
    # Barra de espaço acrescenta Pontos na posição atual do mouse
    if key == ' ':
        pontos.add(Ponto(mouseX, mouseY))  # acrescenta Ponto no set
    # 'd' remove os Pontos previamente selecionandos com clique, marcados em preto.
    if key == 'd':
        for ponto in pontos:
            # se a lista tiver pelo menos 2 pontos
            if ponto.sel and len(pontos) > 1:
                pontos.remove(ponto)           # remove pontos selecionados
        for aresta in arestas:
            if aresta.sel:  # se a lista tiver pelo menos 2 pontos
                arestas.remove(aresta)           # remove pontos selecionados

def mouseDragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

class Ponto():

    " Pontos num grafo, VEL_MAX inicial sorteada, criam Arestas com outros Pontos "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.z = 0  # para compatibilidade com PVector...
        self.vx = random(-VEL_MAX, VEL_MAX)
        self.vy = random(-VEL_MAX, VEL_MAX)
        self.sel = False   # se está selecionado, começa sem seleção
        self.cor = color(random(128, 255),  # R
                         random(128, 255),  # G
                         random(128, 255),  # B
                         128)              # Alpha ~50%
        self.cria_arestas()

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            noStroke()
        fill(self.cor)
        ellipse(self.x, self.y, TAM_PONTO, TAM_PONTO)
        if dist(mouseX, mouseY, self.x, self.y) < TAM_PONTO:
            stroke(255)
            noFill()
            ellipse(self.x, self.y, TAM_PONTO + 5, TAM_PONTO + 5)
            # fill(0)
            # text(str(len(pontos)) + " " + str(len(arestas)), self.x, self.y)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx, VEL_MAX)
        self.vy = self.limitar(self.vy, VEL_MAX)

    def cria_arestas(self, modo='random'):
        if modo == 'random':
            lista_pontos = list(pontos)
            if lista_pontos:
                nova_aresta = Aresta(rnd.choice(lista_pontos), self)
                arestas.append(nova_aresta)
        elif modo == 'all':
            for ponto in pontos:
                nova_aresta = Aresta(ponto, self)
                arestas.append(nova_aresta)

    def limitar(self, v, v_max):
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v

class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.sel = False

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            stroke(255)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        noStroke()
        fill(255)
        ellipse(self.p1.x, self.p1.y, TAM_PONTO / 6, TAM_PONTO / 6)
        ellipse(self.p2.x, self.p2.y, TAM_PONTO / 6, TAM_PONTO / 6)

    def puxa_empurra(self):
        d = dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        delta = TAM_BARRA - d
        dir = PVector.sub(self.p1, self.p2)
        dir.mult(delta / 1000)
        self.p1.vx = self.p1.vx + dir.x
        self.p1.vy = self.p1.vy + dir.y
        self.p2.vx = self.p2.vx - dir.x
        self.p2.vy = self.p2.vy - dir.y


def pointInsideLine(thePoint, theLineEndPoint1, theLineEndPoint2, theTolerance):
    # from Andreas Schlegel / http://www.sojamo.de """
    dir = PVector(theLineEndPoint2.x, theLineEndPoint2.y, 0)
    dir.sub(theLineEndPoint1)
    diff = PVector(thePoint.x, thePoint.y, 0)
    diff.sub(theLineEndPoint1)
    try:
        insideDistance = diff.dot(dir) / dir.dot(dir)
    except ZeroDivisionError:
        insideDistance = 1000
    if (0 < insideDistance < 1):
        closest = PVector(theLineEndPoint1.x, theLineEndPoint1.y, 0)
        dir.mult(insideDistance)
        closest.add(dir)
        d = PVector(thePoint.x, thePoint.y)
        d.sub(closest)
        distsqr = d.dot(d)
        return (distsqr < pow(theTolerance, 2))
    return False
