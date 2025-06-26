# To run inside FreeCAD.org
from random import randint

import Part
from FreeCAD import Vector

Gui.runCommand('Std_SelectAll',0)
Gui.runCommand('Std_Delete')

largura = 100
altura = 200
espessura = 10
espaco = 10

colunas = int(largura / espaco)
filas = int(altura / espaco)

placa = Part.makeBox(largura, altura, espessura)

for coluna in range(colunas):
    x = coluna * espaco + espaco / 2
    for fila in range(filas):
        y = fila * espaco + espaco / 2
        pos = Vector(x, y, -espessura / 2)
        raio = randint(1, 4) 
        furador = Part.makeCylinder(raio, espessura * 2, pos)
        placa = placa.cut(furador)

Part.show(placa)

