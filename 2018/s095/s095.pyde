# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s095"  # 180405

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from graphs import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    size(600, 600)
    frameRate(30)
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino)

    Ponto.reset_SET(int(input.analog(2) / 4))  # cria um set vazio e popula

def draw():
    background(0)

    TAM_ARESTA = input.analog(1) / 4
    NUM_PONTOS = int(input.analog(2) / 4)
    VEL_MAX = input.analog(3) / 128
    CONNECT_RATE = 0.5 + input.analog(4) / 256  # % of connections

    # para cada ponto
    for ponto in Ponto.SET:
        ponto.desenha()  # desenha
        ponto.move(VEL_MAX)    # atualiza posição
    # checa arestas, se OK desenhar, se nãotem pontos removidos ou iguais
    COM_ARESTAS = set()  # para guardar pontos com aresta
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET)\
                or (aresta.p1 is aresta.p2):  # arestas degeneradas
            Aresta.ARESTAS.remove(aresta)   # remove a aresta
        else:                # senão, tudo OK!
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra(TAM_ARESTA)  # altera a velocidade dos pontos
            # Adiciona ao conjunto de pontos com aresta
            COM_ARESTAS.update([aresta.p1, aresta.p2])
    SEM_ARESTAS = Ponto.SET - COM_ARESTAS  
    print( len(Ponto.SET), len(SEM_ARESTAS), len(COM_ARESTAS))
    # atualiza número de pontos
    NUM_ATUAL = len(Ponto.SET)
    if NUM_PONTOS > NUM_ATUAL:
        Ponto.SET.add(Ponto(random(width), random(height)))
    elif NUM_PONTOS < NUM_ATUAL - 2:
        for _ in range (NUM_ATUAL - 2 - NUM_PONTOS): 
            if SEM_ARESTAS:
                remover = SEM_ARESTAS.pop()
                Ponto.SET.remove(remover)
            else:
                Ponto.SET.pop()
    # atualiza número de arestas
    if int((NUM_PONTOS) * CONNECT_RATE) > len(Aresta.ARESTAS) + 1:
        rnd_choice(list(Ponto.SET)).cria_arestas()
    elif int(NUM_PONTOS * CONNECT_RATE) < len(Aresta.ARESTAS) - 1:
        Aresta.ARESTAS.remove(rnd_choice(Aresta.ARESTAS))

    if input.digital(13):
        Ponto.reset_SET(int(input.analog(2) / 4))

    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 30 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=500,
                                filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    input.update()

def mouseDragged():        # quando o mouse é arrastado
    for ponto in Ponto.SET:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
