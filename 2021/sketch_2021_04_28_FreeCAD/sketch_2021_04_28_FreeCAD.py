import Part
from FreeCAD import Vector

largura, altura, espessura = 50, 80, 10
plate = Part.makeBox(largura, altura, espessura)
espaco, raio = 10, 4
furador = Part.makeCylinder(raio, espessura * 2, Vector(0, 0, -espessura / 2))

for x in range(0, largura, espaco):
    for y in range(0, altura, espaco):
        furo = furador.translated(Vector(x + espaco / 2, y + espaco / 2, 0))
        plate = plate.cut(furo)

Part.show(plate)
