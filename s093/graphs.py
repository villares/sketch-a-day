# -*- coding: utf-8 -*-
TAM_PONTO = 50  # TAM_PONTO dos Pontos 

class Ponto():
    VEL_MAX = 5
    SET = set()

    " Pontos num grafo, VEL_MAX inicial sorteada, criam Arestas com outros Pontos "

    def __init__(self, x, y, cor=color(0)):
        VEL_MAX = Ponto.VEL_MAX
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

    def move(self, VEL_MAX):
        Ponto.VEL_MAX = VEL_MAX
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx, VEL_MAX)
        self.vy = self.limitar(self.vy, VEL_MAX)

    def cria_arestas(self):
            lista_pontos = list(Ponto.SET)
            if lista_pontos:
                nova_aresta = Aresta(rnd_choice(lista_pontos), self)
                Aresta.ARESTAS.append(nova_aresta)

    def limitar(self, v, v_max):
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v

class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    ARESTAS = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def desenha(self):
        stroke(0)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        noStroke()
        fill(0)
        ellipse(self.p1.x, self.p1.y, TAM_PONTO / 6, TAM_PONTO / 6)
        ellipse(self.p2.x, self.p2.y, TAM_PONTO / 6, TAM_PONTO / 6)

    def puxa_empurra(self, TAM_BARRA):
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
