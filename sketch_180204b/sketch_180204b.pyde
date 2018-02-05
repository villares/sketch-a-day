from __future__ import division, unicode_literals

CONFETI = []
SIZE = 15
TEXTO = """CARNAHACKING VEM AÍ"""

def settings():
    #global fundo
    #fundo = loadImage("p.jpg")
    #size(fundo.width, fundo.height)
    size(500, 500)

def setup():
    noStroke()
    for _ in range(1200):
        CONFETI.append(([random(width),  # X
                         random(height+20)],  # Y
                        random(TWO_PI),  # screen plane rotation
                        random(TWO_PI),  # "Z" rotation
                        color(random(256), random(256), random(256))  # color
                        ))

def draw():
    #background(fundo)
    background(0)

    for pos, rot1, rot2, color_ in CONFETI:
        #print (pos, r1, r2, c)
        with pushMatrix():
            x, y = pos
            translate(x, y)
            rotate(rot1 + float(frameCount / 7))
            s = sin(rot2 + float(frameCount / 11))
            fill(color_)
            ellipse(0, 0, SIZE, SIZE * s)
            pos[1] += 1 + random(0, 2) * s # update y (pos[1])
            if y > height + 20:
                pos[1] = -20
    if frameCount<300 and not frameCount % 3: saveFrame("###.tga")

    