"""
Prova de conceito para mapa em 3D
"""

# Para pau com placa Intel HD
from java.lang import System
System.setProperty("jogl.disable.openglcore", "false")

from mapa import Quadrado

mapa = {}
Quadrado.tamanho = 15  # tamanho grade
Quadrado.mapa = mapa

def setup():
    global colunas, filas
    size(600, 600, P3D)
    colunas = width / Quadrado.tamanho
    filas = height / Quadrado.tamanho
    setup_mapa()
    
def setup_mapa():
    global mapa
    mapa.clear()
    for fila in range(filas):
        for coluna in range(colunas):
            mapa[(coluna, fila)] = Quadrado(coluna, fila)
    for quadrado in mapa.values():
            quadrado.calcula_vizinhos()
    for fila in range(filas):
        for coluna in range(colunas):
            mapa[(coluna, fila)].define_tipo()
    # for quadrado in mapa.values():
    #         quadrado.define_tipo()
    for quadrado in mapa.values():
            quadrado.calcula_alturas()
     
def draw():
    background(0)
    lights()

    # camera(width / 2, height / 2, 500.0,  # eyeX, eyeY, eyeZ
    camera(width / 2, mouseY*2, 500.0,  # eyeX, eyeY, eyeZ
           width / 2, height / 2, 0.0,        # centerX, centerY, centerZ
           0.0, 1.0, 0.0)        # upX, upY, upZ
    for fila in range(filas):
        for coluna in range(colunas):
            mapa[(fila, coluna)].desenha()
            
def keyPressed():
    if key == ' ':
        setup_mapa()
