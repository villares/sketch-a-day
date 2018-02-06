"""
s33 180204b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

from __future__ import division

CONFETI = []
SIZE = 15

def setup():
    size(500, 500)
    noStroke()
    for _ in range(1200):
        CONFETI.append(([random(width),        # [X,
                         random(height + 20)], #  Y] -> x, y position list
                        random(TWO_PI),  # screen plane rotation
                        random(TWO_PI),  # "Z" rotation
                        color(random(256), random(256), random(256)) # color
                        ))

def draw():
    background(0)

    for position, rot1, rot2, color_ in CONFETI:
        with pushMatrix():  # contexto do sistema de coordenadas mudado
            x, y = position  # umpack da lista position
            translate(x, y)  # translada sistema de coordenadas
            rotate(rot1 + float(frameCount / 7))
            s = sin(rot2 + float(frameCount / 11))
            fill(color_)
            ellipse(0, 0, SIZE, SIZE * s)
            position[1] += 1 + random(0, 2) * s  # update y (position[1])
            if y > height + 20:
                position[1] = -20

    # if frameCount<200 and frameCount % 2
    # saveFrame("###.tga") # salva frames para o GIF
