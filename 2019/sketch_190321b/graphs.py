# -*- coding: utf-8 -*-
from random import choice

TAM_PONTO = 30  # TAM_PONTO dos Pontos 

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
        self.cor = choice((color(255), color(0), color(0, 0, 200)))
        self.cria_arestas()
        self.r = choice((10, 20, 40))
        
    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def desenha(self):
        pass
        # noStroke()
        # stroke(255)
        # noFill()
        # ellipse(self.x, self.y, TAM_PONTO, TAM_PONTO)

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
            if len(lista_pontos) > 1:
                rnd_ponto = choice(lista_pontos)
                while rnd_ponto == self:
                    rnd_ponto = choice(lista_pontos)
            
                Aresta.ARESTAS.append(Aresta(rnd_ponto, self))

    def limitar(self, v, v_max):
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v


class Aresta():

    """ Arestas contém só dois Pontos """            

    ARESTAS = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def desenha(self):
        strokeWeight(2)
        stroke(lerpColor(self.p1.cor, self.p2.cor, 0.5))
        noFill()
        wave(self.p1.x, self.p1.y, self.p2.x, self.p2.y,
                self.p1.r, self.p2.r)
        noStroke()
        fill(0)
        # fill(self.p1.cor)
        ellipse(self.p1.x, self.p1.y, TAM_PONTO / 4, TAM_PONTO / 4)
        # fill(self.p2.cor)
        ellipse(self.p2.x, self.p2.y, TAM_PONTO / 4, TAM_PONTO / 4)

    def puxa_empurra(self, TAM_BARRA):
        d = dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        delta = TAM_BARRA - d
        dir = PVector.sub(self.p1, self.p2)
        dir.mult(delta / 1000)
        self.p1.vx = self.p1.vx + dir.x
        self.p1.vy = self.p1.vy + dir.y
        self.p2.vx = self.p2.vx - dir.x
        self.p2.vy = self.p2.vy - dir.y

def wave(x1, y1, x2, y2, s=None, n=2):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = dist(x1, y1, x2, y2)
    if not s:
        s = int(max(L / 5, 10))
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = 0
        dy = L / (n+2)
        line(0, 0, 0, dy)
        for i in range(1, n+1):
            if i % 2: 
                line(0, i * dy, -s, i * dy + dy/2)
                line(0, i * dy + dy,  -s, i * dy + dy/2.)
            else:
                line(0, i * dy, s, i * dy + dy/2)
                line(0, i * dy + dy,  s, i * dy + dy/2.)   
        line(0, L, 0, L- dy)
