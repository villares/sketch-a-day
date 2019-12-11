# -*- coding: utf-8 -*-
# Paleta B - grupo 1
coresB = ((0, 255, 77), (109, 0, 255), (255, 0, 255),
          (0, 255, 255), (255, 0, 71), (253, 255, 0))

# Paleta A - grupo 2
coresA = ((255, 82, 0), (255, 247, 0), (0, 238, 255),
          (79, 0, 255), (0, 255, 249), (255, 255, 255))

# Paleta C - grupo 3
coresC = ((224, 0, 255), (255, 245, 0), (0, 255, 241),
          (255, 0, 95), (255, 250, 0), (255, 255, 255))


def paleta(ins, valor):
    opcoes = (coresB[:3],
              coresB[3:],
              coresA[:3],
              coresA[3:],
              coresC[:3],
              coresC[3:],
              )
    if ins > 5:
        ins = 5
    a, b, c = opcoes[ins]
    return triangulo(color(*a), color(*b), color(*c), int(valor))

def triangulo(a, b, c, v):
    if 0 <= v < 60 or v == 360:
        return a
    if 60 <= v < 120:
        t = map(v, 60, 120, 0, 1)
        return lerpColor(a, b, t)
    if 120 <= v < 180:
        return b
    if 180 <= v < 240:
        t = map(v, 180, 240, 0, 1)
        return lerpColor(b, c, t)
    if 240 <= v < 300:
        return c
    if 300 <= v < 360:
        t = map(v, 300, 360, 0, 1)
        return lerpColor(c, a, t)
