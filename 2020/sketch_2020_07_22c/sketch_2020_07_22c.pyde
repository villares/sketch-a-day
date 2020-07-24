"""
Prova de conceito para mapa em 3D
"""
from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

import random as rnd

TAMANHO = 25  # tamanho grade
mapa = []

def setup():
    global mapa, COLUNAS, FILAS
    size(500, 500, P3D)
    COLUNAS = width / TAMANHO
    FILAS = height / TAMANHO
    for fila in range(FILAS):
        for coluna in range(COLUNAS):
            tipo = rnd.choice(Quadrado.TIPOS)
            altura = sorteiaAltura(tipo)
            quadrado = Quadrado(fila, coluna, tipo, altura)
            mapa.append(quadrado)

def draw():
    background(0)
    camera(width / 2, mouseY * 2, 500.0,  # eyeX, eyeY, eyeZ
           width / 2, height / 2, 0.0,        # centerX, centerY, centerZ
           0.0, 1.0, 0.0)        # upX, upY, upZ
    
    for quadrado in mapa:
            quadrado.desenha()
    '''
    for fila in range(FILAS):
        for coluna in range(COLUNAS):
            quadrado = no_mapa(fila, coluna)
            quadrado.desenha()
    '''
    
class Quadrado():

    ''' Região quadrada do mapa'''

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

    def __init__(self, fila, coluna, tipo, altura):
        self.fila = fila
        self.coluna = coluna
        self.tipo = tipo
        self.altura = altura
        self.cor = Quadrado.CORES[tipo]

    def desenha(self):
        posX, posY = self.coluna * TAMANHO, self.fila * TAMANHO
        with pushMatrix():
            translate(posX, posY)
            noStroke()
            fill(self.cor)
            pushMatrix()
            translate(0, 0, self.altura)
            rect(0, 0, TAMANHO, TAMANHO)
            popMatrix()
            fill(255)       # branco
            textSize(20)  # para escrever o tipo se o mouse estiver perto
            textAlign(CENTER, CENTER)
            if (dist(posX, posY, mouseX, mouseY) < TAMANHO * 2):
                text(self.tipo, TAMANHO / 2, TAMANHO / 2, self.altura + 5)

def no_mapa(fila, coluna):
    return mapa[coluna + fila * COLUNAS]

def sorteiaAltura(tipo):
    # return 0 #(para demo plana)
    if tipo == "S" or tipo == "B":
        return 0
    elif tipo == "M":
        return 30
    else:
        return random(5, 25)
