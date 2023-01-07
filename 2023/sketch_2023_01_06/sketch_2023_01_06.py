"""
Intrincado padrão de pixels coloridos sobre fundo preto, baseado na expressã  (abs((x + y) ^ (x - y)) ** a) % b

Onde ^ é o operador XOR binário
% b produz o resto da divisão por b

D'aprés @ntsutae つぶやきProcessing
https://twitter.com/ntsutae/status/1268432505356513280?s=20
Que por sua vez se inspirou em 
https://www.dwitter.net/d/18851
"""

a, b, c = 1.9, 512, 256

def setup():
    size(1024, 1023)
    no_smooth()
    color_mode(HSB)

def draw():
    background(0)
    s = 1
    scale(s)
    w = width // s
    for x in range(w):
        for y in range(w):
            p = (abs((x + y) ^ (x - y)) ** a) % b
            if p < c:
                px = color(p % 256, 255, 255)
                stroke(px)
                point(x, y)


def key_pressed():
    global a, b, c
    if key == 'a':
        a += .1
    if key == 'z' and a > 1:
        a -= .1
    if key == 's':
        b += 1
    if key == 'x' and b > 1:
        b -= 1
    if key == 'd':
        c += 1
    if key == 'c' and c > 1:
        c -= 1
    print(a, b, c)
    if key == ' ':
        save(f'{a}_{b}_{c}.png')

# First ported from @ntsutae code for a single tweet
# t=0;w=720#つぶやきProcessing d'aprés @ntsutae
# def setup():size(w,w)
# def draw():
#  global t;t+=1;scale(3);background(-1)
#  for y in range(240):
#   for x in range(240):
#    (t+abs((x+y-t)^(x-y+t))**3)%1023<109 and point(x,y)
