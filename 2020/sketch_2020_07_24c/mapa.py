# -*- coding: utf-8 -*-

from random import choice

AMARELO = color(255, 230, 0)
AZUL_ESCURO = color(7, 0, 255)
MARROM_ESCURO = color(85, 25, 27)
VERDE_CLARO = color(10, 237, 7)
MARROM_CLARO = color(193, 109, 111)
VERDE_ESCURO = color(48, 72, 36)
TIPOS = {"sea": AZUL_ESCURO,
         "mount": MARROM_ESCURO,
         "shore": AMARELO,
         "field": VERDE_CLARO,
         "town": MARROM_CLARO,
         "forest": VERDE_ESCURO}

PROB_TIPOS = {"sea": ["sea"] * 10 + ["shore"] * 2,
              "mount":["forest"] * 10 + ["town"] * 2,
              "shore": ["field"] * 10 + ["town"] * 2,
              "field": ["forest"] * 10 + ["shore"] * 2,
              "town": ["field"] * 10 + ["forest"] * 2,
              "forest": ["field"] * 10 + ["mount"] * 2,
              }

class Quadrado():

    """ Região quadrada do mapa"""

    def __init__(self, coluna, fila):
        self.fila = fila
        self.coluna = coluna
        self.tipo = None

    def define_tipo(self):
        pool_tipos = [] #[choice(TIPOS.keys())] # ["mount"] #TIPOS.keys()
        # print(pool_tipos)
        for v in self.vizinhos:
            if v.tipo is not None:
                # print(v.tipo)
                pool_tipos.extend(PROB_TIPOS[v.tipo])
        if not pool_tipos:
            pool_tipos = [choice(TIPOS.keys())]
            print(pool_tipos, self.coluna, self.fila)
            
        self.tipo = choice(pool_tipos)

        self.altura = Quadrado.sorteiaAltura(self.tipo)
        self.cor = TIPOS[self.tipo]

    def desenha(self):
        tam = self.tamanho
        posX, posY = self.coluna * tam, self.fila * tam
        with pushMatrix():
            translate(posX, posY)
            noStroke()
            fill(self.cor)

            pos = ((-1, -1), (1, -1), (1, 1), (-1, 1))
            for i, c in enumerate(self.alturas_cantos):
                pc = self.alturas_cantos[i - 1]
                ipos, ppos = pos[i], pos[i - 1]
                beginShape()
                vertex(ipos[0] * tam / 2, ipos[1] * tam / 2, c)
                vertex(ppos[0] * tam / 2, ppos[1] * tam / 2, pc)
                vertex(0, 0, self.altura)
                endShape(CLOSE)
            # translate(0, 0, self.altura)
            # rect(0, 0, self.tamanho, self.tamanho)

            textSize(18)  # para escrever o tipo se o mouse estiver perto
            textAlign(CENTER, CENTER)
            if (dist(posX, posY, mouseX, mouseY) < self.tamanho):
                fill(255)
                text(self.tipo[:3].upper(), self.tamanho / 2 - 1, self.tamanho / 2 - 1, 36)

    def calcula_vizinhos(self):
        """
        Calcula uma lista self.vizinhos (incluindo 'S', self)
        e self.grupos_cantos (0TLS, T1RS, SR2B, LSB3)

            0 | T | 1
            --|---|--
            L | S | R
            --|---|--
            3 | B | 2
        """
        TL = ((-1, -1), (0, -1), (-1, 0), (0, 0))
        TR = ((+1, -1), (0, -1), (+1, 0), (0, 0))
        BL = ((-1, +1), (0, +1), (-1, 0), (0, 0))
        BR = ((+1, +1), (0, +1), (+1, 0), (0, 0))
        self.grupos_cantos = [[self.mapa[(self.coluna + i, self.fila + j)]
                               for i, j in posicoes
                               if self.mapa.get((self.coluna + i, self.fila + j))]
                              for posicoes in (TL, TR, BR, BL)]
        TODOS = ((-1, -1), (+0, -1), (+1, -1),
                 (-1, +0), (+0, +0), (+1, +0),
                 (-1, +1), (+0, +1), (+1, +1))
        self.vizinhos = [self.mapa[(self.coluna + i, self.fila + j)]
                         for i, j in TODOS
                         if self.mapa.get((self.coluna + i, self.fila + j))]

    def calcula_alturas(self):
        self.alturas_cantos = []
        for grupo in self.grupos_cantos:
            alturas = [quadrado.altura for quadrado in grupo]
            if all(alturas):
                media_alturas = sum(alturas) / len(alturas)
            else:
                media_alturas = 0
            self.alturas_cantos.append(media_alturas)

    @staticmethod
    def sorteiaAltura(tipo):
        # return 0 #(para demo plana)
        if tipo == "sea" or tipo == "shore":
            return 0
        elif tipo == "mount":
            return 30
        else:
            return random(5, 25)
