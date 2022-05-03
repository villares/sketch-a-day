import Part
from FreeCAD import Vector

from random import choice

dims = (40, 60, 80, 100)

parede = 10

paredes, furos = [], []

for _ in range(10):
    largura, altura, espessura = choice(dims), choice(dims), choice(dims)
    box = Part.makeBox(largura, altura, espessura)
    box.translate(Vector(-largura / 2, -altura / 2, 0))        
    paredes.append(box)
    furo = Part.makeBox(largura - parede, altura - parede, espessura)
    furo.translate(Vector(parede / 2, parede / 2))
    #result = box.cut(furo)
    furo.translate(Vector(-largura / 2, -altura / 2, 0))
    furos.append(furo)

union_furos = furos.pop()
for f in furos:
    union_furos = union_furos.fuse(f)

union_paredes = paredes.pop()
for p in paredes:
    union_paredes = union_paredes.fuse(p)

result = union_paredes.cut(union_furos)

Part.show(result)
