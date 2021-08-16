# shoebot (code to be run with sbot runner)

from math import *
from random import randint
PI, QUARTER_PI, HALF_PI = pi, pi / 4, pi / 2
frame_count = 0

def setup():
    size(600, 600)
    strokewidth(1)
    colorrange(255)
    speed(1)
    
def draw():
    global frame_count
    background(200)
    stroke(0)
    pontos = []
    for i in range(12):
        r = randint(WIDTH / 10, WIDTH / 4)
        xo = randint(r, WIDTH - r)
        yo = randint(r, HEIGHT - r)
        for a in range (36):
            x = xo + r * sin(radians(a * 10))
            y = yo + r * cos(radians(a * 10))
            pontos.append((x, y))
    for xa, ya in pontos:
        for xb, yb in pontos:
            not_same = (xa, ya) != (xb, yb)
            if not_same and dist((xa, ya), (xb, yb)) < 50:
                line(xa, ya, xb, yb)

    

    frame_count += 1
    
# def seta(xa, ya, xb, yb):
#     tam_seta = dist((xa, ya), (xb, yb))
#     ang = atan2(yb - ya, xb - xa)    
#     xai, yai = lerp_tuple((xa, ya), (xb, yb), 1 / 3.0)
#     xaf, yaf = lerp_tuple((xa, ya), (xb, yb), 2 / 3.0)
#     amp = 20 * sin(frame_count / 10.0)
#     xout = cos(ang + HALF_PI) * amp
#     yout = sin(ang + HALF_PI) * amp
#     nofill()
#     autoclosepath(False)
#     beginpath(xa, ya)
#     lineto(xai, yai)
#     lineto(xai + xout, yai + yout)
#     lineto(xaf + xout, yaf + yout)
#     lineto(xaf, yaf)    
#     lineto(xb, yb)
#     endpath()
#     tam_ponta = tam_seta / 10 * sqrt(2)
#     xpe = xb + cos(ang + QUARTER_PI + PI) * tam_ponta
#     ype = yb + sin(ang + QUARTER_PI + PI) * tam_ponta
#     xpd = xb + cos(ang - QUARTER_PI + PI) * tam_ponta
#     ypd = yb + sin(ang - QUARTER_PI + PI) * tam_ponta
#     beginpath(xpe, ype)    
#     lineto(xb, yb) # parte esquerda da ponta
#     lineto(xpd, ypd) # parte direita da ponta
#     endpath()
    
def lerp(a, b, t):
    return a * (1 - t) + b * t

    
def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))