# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s091"  # 180401

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import gif_export
from shapes import *
from parameters import *

SHAPES = [circle,  # defined in shapes.py
          square,
          exes,
          losang]


pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

TAM_PONTO = 50  # TAM_PONTO dos Pontos \
TAM_BARRA = 100
VEL_MAX = 2  # velocidade máxima nas ortogonais vx e vy
NUM_PONTOS = 5
NUM_CONNECT = 1

def setup():
    frameRate(30)
    background(0)
    global A, B, C, D
    # Ask user for Arduino port, cancel will return `None`
    port = Inputs.select_source(Arduino)
    # `None` will activate Sliders
    A, B, C, D = Inputs.setup_inputs(port)

    size(400, 400)
    fill(0)

    for _ in range(NUM_PONTOS):
        x, y = random(width), random(height)
        pontos.add(Ponto(x, y))  # acrescenta um Ponto


def draw():
    global TAM_BARRA, NUM_PONTOS, VEL_MAX, NUM_CONNECT
    background(128)        # limpa a tela

    TAM_BARRA = A.val / 4
    NUM_PONTOS = int(B.val / 4)
    VEL_MAX = C.val / 128
    NUM_CONNECT = 1+ int(D.val / 256)
    update_num_pontos()

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

    # if Inputs.TILT:
    #     background(128)

    # uncomment next lines to export GIF
    if not frameCount % 30:
         gif_export(GifMaker,
                    frames=2000,
                    delay=500,
                    filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    Inputs.update_inputs()


# Sob clique do mouse seleciona/deseleciona Pontos ou Arestas
def mouseClicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção
    mouse = PVector(mouseX, mouseY)

def keyPressed():   # Quando uma tecla é pressionada
    # Barra de espaço acrescenta Pontos na posição atual do mouse
    if key == ' ':
        pontos.add(Ponto(mouseX, mouseY))  # acrescenta Ponto no set

def mouseDragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

def update_num_pontos():
    print(NUM_PONTOS, len(pontos), NUM_CONNECT)
    if NUM_PONTOS > len(pontos):
        pontos.add(Ponto(random(width), random(height)))
    elif NUM_PONTOS < len(pontos):
        pontos.remove(rnd_choice(list(pontos)))


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

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx, VEL_MAX)
        self.vy = self.limitar(self.vy, VEL_MAX)

    def cria_arestas(self):
        for _ in range(NUM_CONNECT):
            lista_pontos = list(pontos)
            if lista_pontos:
                nova_aresta = Aresta(rnd_choice(lista_pontos), self)
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

def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
