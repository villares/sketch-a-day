# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s091"  # 180401

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import gif_export
from graphs import *
from parameters import *

def setup():
    frameRate(30)
    global A, B, C, D
    # Ask user for Arduino port, cancel will return `None`
    port = Inputs.select_source(Arduino)
    # `None` will activate Sliders
    A, B, C, D = Inputs.setup_inputs(port)

    size(400, 400)

def draw():
    background(128) 

    TAM_BARRA   =         A.val / 4
    NUM_PONTOS  =     int(B.val / 4)
    VEL_MAX     =         C.val / 128
    NUM_CONNECT =     1+    int(D.val / 256) # % of connections

    # para cada ponto
    for ponto in Ponto.SET:
        ponto.desenha()  # desenha
        ponto.move(VEL_MAX)    # atualiza posição
    # para cada aresta
    # checa se há Arestas com Pontos já removidos
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET):
            Aresta.ARESTAS.remove(aresta)   # nesse caso remove a Aresta também
        else:                # senão
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra(TAM_BARRA)  # altera a velocidade dos pontos
    # atualiza número de pontos
    if NUM_PONTOS > len(Ponto.SET):
        Ponto.SET.add(Ponto(random(width), random(height)))
    elif NUM_PONTOS < len(Ponto.SET):
        Ponto.SET.remove(rnd_choice(list(Ponto.SET)))
    # atualiza número de arestas
    if NUM_PONTOS * NUM_CONNECT > len(Aresta.ARESTAS):
        rnd_choice(list(Ponto.SET)).cria_arestas()
    elif NUM_PONTOS * NUM_CONNECT < len(Aresta.ARESTAS):
        Ponto.SET.remove(rnd_choice(list(Ponto.SET)))
    
    if Inputs.TILT:
        Ponto.SET = set()

    # uncomment next lines to export GIF
    if not frameCount % 30:
         gif_export(GifMaker,
                    frames=2000,
                    delay=500,
                    filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    Inputs.update_inputs()

def mouseDragged():        # quando o mouse é arrastado
    for ponto in Ponto.SET:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0
