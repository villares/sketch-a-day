# -*- coding: utf-8 -*-
from random import choice
from arcs import *

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
        colorMode(HSB)
        self.cor = color(random(256), 255, 255)
        self.cria_arestas()
        self.r = choice((10, 20, 40))
        
    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def desenha(self):
        pass

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
        
    @staticmethod
    def reset_all(num):
        Ponto.SET = set()
        for _ in range(num):
            Ponto.SET.add(Ponto(width / 2, height / 2))


class Aresta():

    """ Arestas contém só dois Pontos """            

    ARESTAS = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # def desenha(self):
    #     strokeWeight(2)
    #     fill(lerpColor(self.p1.cor, self.p2.cor, 0.5))
    #     stroke(0)
    #     var_bar(self.p1.x, self.p1.y, self.p2.x, self.p2.y,
    #             self.p1.r, self.p2.r)
    #     noStroke()
    #     fill(0)
    #     # fill(self.p1.cor)
    #     ellipse(self.p1.x, self.p1.y, TAM_PONTO / 4, TAM_PONTO / 4)
    #     # fill(self.p2.cor)
    #     ellipse(self.p2.x, self.p2.y, TAM_PONTO / 4, TAM_PONTO / 4)

    def puxa_empurra(self, TAM_BARRA):
        d = dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        delta = TAM_BARRA - d
        dir = PVector.sub(self.p1, self.p2)
        dir.mult(delta / 1000)
        self.p1.vx = self.p1.vx + dir.x
        self.p1.vy = self.p1.vy + dir.y
        self.p2.vx = self.p2.vx - dir.x
        self.p2.vy = self.p2.vy - dir.y
