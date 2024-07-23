from pytop5js import *

w = h = d = 1

# Cubo
max_w = 200
max_h = 200
max_d = 200

# plano B - Paralelepípedo
# max_w = 100
# max_h = 150
# max_d = 50

pausa = 100

def setup():
    createCanvas(500, 500, WEBGL)
    noFill()
    strokeWeight(5)
    
def draw():
    global w, h, d  # para modificar variáveis globais em Python
    background(200) # fundo e limpa frame
    #translate(250, 250) # muda origem das coordenadas para o centro da tela
    # giro quando o cubo cresce
    rotateX((d - 1) / 100.)
    rotateZ((d - 1) / 100.)
    # desenha a "caixa" (ponto, linha, retêngulo e caixa...)
    box(h, w, d)
    
    if w < max_w:
        if frameCount > pausa:
            w += 1
    elif h < max_h:
        if frameCount > 2 * pausa + max_w:
            h += 1
    elif d < max_d:
        if frameCount > 3 * pausa + max_w + max_h:
            d += 1
    else:
        noLoop()


# This is required by pyp5js to work
start_p5(setup, draw)
