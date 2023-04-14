from collections import deque

pontos = deque(maxlen=400)   # últimos 200 pontos

def setup():        # executa uma vez no começo
    size(600, 600)  # tamanho da tela
    no_fill()   # sem preenchimento
    color_mode(HSB)
    
def draw():         # repete a cada quadro
    background(100, 0, 0)  # limpa fundo com vermelho
    for i, (x, y) in enumerate(pontos):  # x, y para cada ponto em pontos
        d = sin(radians(i + frame_count)) * 50 + 50
        stroke(d * 3, 200, 200)   # cor do traço
        circle(x, y, d)    # desenho círculo (onde passou o mouse)
    
def mouse_dragged():  # executa só quando o mouse é arrastado
    pos = (mouse_x, mouse_y) # tupla do x e y do mouse
    pontos.append(pos) # pontos acrescente pos no seu final
    
def key_pressed():
#     global pontos
#     if key == ' ':
#         pontos = [] # reatribuição requer instrução "global pontos" antes
    if key == ' ':
        pontos.clear()