# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s094"  # 180404

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import gif_export
from graphs import *
from parameters import *

def setup():
    global A, B, C, D
    size(400, 400)
    frameRate(30)
    # Ask user for Arduino port, cancel will return `None`
    port = Inputs.select_source(Arduino)
    # `None` will activate Sliders
    A, B, C, D = Inputs.setup_inputs(port)

    Ponto.reset_SET(int(B.val / 4))  # cria um set vazio e popula

def draw():
    background(200)

    TAM_BARRA = A.val / 4
    NUM_PONTOS = int(B.val / 4)
    VEL_MAX = C.val / 128
    CONNECT_RATE = 0.5 + D.val / 256  # % of connections

    # para cada ponto
    for ponto in Ponto.SET:
        ponto.desenha()  # desenha
        ponto.move(VEL_MAX)    # atualiza posição
    # para cada aresta checa se pode desenhar, se não teve pontos já removidos
    # ou pontos iguais
    COM_ARESTAS = set()  # para guardar pontos com aresta
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET)\
                or (aresta.p1 is aresta.p2):  # arestas degeneradas
            Aresta.ARESTAS.remove(aresta)   # remove a aresta
        else:                # senão
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra(TAM_BARRA)  # altera a velocidade dos pontos
            # Adiciona ao conjunto de pontos com aresta
            COM_ARESTAS.update([aresta.p1, aresta.p2])
    Ponto.SET = COM_ARESTAS  # isto remove pontos sem nenhuma aresta
    # atualiza número de pontos
    if NUM_PONTOS > len(Ponto.SET):
        Ponto.SET.add(Ponto(random(width), random(height)))
    # elif NUM_PONTOS < len(Ponto.SET) - 10:
    #     print (NUM_PONTOS, len(Ponto.SET))
    #     rnd_ponto = rnd_choice(list(Ponto.SET))
    #     Ponto.SET.remove(rnd_ponto)

    # atualiza número de arestas
    if int((NUM_PONTOS) * CONNECT_RATE) > len(Aresta.ARESTAS) + 1:
        rnd_choice(list(Ponto.SET)).cria_arestas()
    elif int(NUM_PONTOS * CONNECT_RATE) < len(Aresta.ARESTAS) - 1:
        Aresta.ARESTAS.remove(rnd_choice(list(Aresta.ARESTAS)))

    if Inputs.TILT:
        Ponto.reset_SET(int(B.val / 4))

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
