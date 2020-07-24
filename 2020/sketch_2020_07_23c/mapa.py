# -*- coding: utf-8 -*-

from random import choice

AMARELO = color(255, 230, 0)
AZUL_ESCURO = color(7, 0, 255)
MARROM_ESCURO = color(85, 25, 27)
VERDE_CLARO = color(10, 237, 7)
MARROM_CLARO = color(193, 109, 111)
VERDE_ESCURO = color(48, 72, 36)
TIPOS = ["S", "M", "B", "P", "V", "F"]
CORES = {"S": AZUL_ESCURO,
         "M": MARROM_ESCURO,
         "B": AMARELO,
         "P": VERDE_CLARO,
         "V": MARROM_CLARO,
         "F": VERDE_ESCURO}

class Quadrado():

    """ Região quadrada do mapa"""

    def __init__(self, coluna, fila, tipo=None):
        self.tipo = tipo or choice(TIPOS)
        self.altura = Quadrado.sorteiaAltura(self.tipo)
        self.fila = fila
        self.coluna = coluna
        self.cor = CORES[self.tipo]

    def desenha(self):
        tam = self.tamanho
        posX, posY = self.coluna * tam, self.fila * tam
        with pushMatrix():
            translate(posX, posY)
            noStroke()
            fill(self.cor)

            pos = ((-1, -1), (1, -1), (1, 1), (-1, 1))
            for i, c in enumerate(self.cantos):
                pc = self.cantos[i - 1]
                ipos, ppos = pos[i], pos[i - 1]
                beginShape()
                vertex(ipos[0] * tam/2, ipos[1] * tam/2, c)
                vertex(ppos[0] * tam/2, ppos[1] * tam/2, pc)
                vertex(0, 0, self.altura)
                endShape(CLOSE)
            # translate(0, 0, self.altura)
            # rect(0, 0, self.tamanho, self.tamanho)

            textSize(20)  # para escrever o tipo se o mouse estiver perto
            textAlign(CENTER, CENTER)
            if (dist(posX, posY, mouseX, mouseY) < self.tamanho * 2):
                fill(0)
                text(self.tipo, self.tamanho / 2, self.tamanho / 2, 35)
                fill(255)
                text(self.tipo, self.tamanho / 2 - 2, self.tamanho / 2 - 2, 36)

    def calcula_cantos(self):
        """
        Devolva uma lista dos cantos nesta ordem:
        0 --- 1
        |     |
        |     |
        3 --- 2
        """
        TL = ((-1, -1), (0, -1), (-1, 0), (0, 0))
        TR = ((+1, -1), (0, -1), (+1, 0), (0, 0))
        BL = ((-1, +1), (0, +1), (-1, 0), (0, 0))
        BR = ((+1, +1), (0, +1), (+1, 0), (0, 0))

        self.cantos = []
        for canto in (TL, TR, BR, BL):
            alturas = [self.mapa[(self.coluna + i, self.fila + j)].altura
                       for i, j in canto
                       if self.mapa.get((self.coluna + i, self.fila + j))]
            print(alturas)
            media = sum(alturas) / len(alturas)
            self.cantos.append(media)

    @staticmethod
    def sorteiaAltura(tipo):
        # return 0 #(para demo plana)
        if tipo == "S" or tipo == "B":
            return 0
        elif tipo == "M":
            return 30
        else:
            return random(5, 25)
