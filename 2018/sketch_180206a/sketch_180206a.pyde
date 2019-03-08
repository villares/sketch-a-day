"""
sketch 37 180206b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

from __future__ import division, unicode_literals

CONFETI = []
SIZE = 15
TEXTO = """carnahacking vem aí""" # ainda não usei este texto...

def settings():    
    #global fundo    
    #fundo = loadImage("p.jpg")
    #size(fundo.width, fundo.height)
    size(500, 500)   # comment out se for usar com fundo

def setup():
    noStroke()
    font = createFont("GaroaHackerClubeBold.otf", 24); 
    textFont(font)
    textAlign(CENTER, CENTER) # Alinhamento horizontal e vertical
    textSize(38)             # Tamanho do texto
    for _ in range(3200):
        CONFETI.append(([random(width),  # X
                         random(height+20)],  # Y
                        random(TWO_PI),  # screen plane rotation
                        random(TWO_PI),  # "Z" rotation
                        color(random(256), random(256), random(256))  # color
                        ))

def draw():
    #background(fundo)
    background(0) # comment out se for usar o fundo
    text(TEXTO, width/2, height/2);

    for pos, rot1, rot2, color_ in CONFETI:
        with pushMatrix():
            x, y = pos
            maxDist = width/2
            dis = dist(x, y, mouseX, mouseY)
            ang = atan2(y - mouseY, x - mouseX)
            if (dis < maxDist):
                dd = map(dis, 0, maxDist, 1, 0)
                dd = pow(dd, 0.9)  * dis * 2
                x += cos(ang) * dd
                y += sin(ang) * dd
            translate(x, y)
            rotate(rot1 + float(frameCount / 7))
            s = sin(rot2 + float(frameCount / 11))
            fill(color_)    
            ellipse(0, 0, SIZE, SIZE * s)
            pos[1] += 1 + random(0, 2) * s # update y (pos[1])
            if y > height + 20:
                pos[1] = -20
            #if dist(x, y, mouseX, mouseY) < 100:
            #      pos[1] += random(-5, 0)
            #      pos[0] += random(-5, 5)
                  
                
    if frameCount<300 and not frameCount % 3: saveFrame("###.tga")

    