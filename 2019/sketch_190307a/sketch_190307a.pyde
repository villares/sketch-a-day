# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "sketch_190307a"  # based on s096 of 180406

add_library('GifAnimation')

from gif_exporter import *
from graphs import *
from inputs import Input
from arcs import poly_rounded2

def setup():
    global input, GIF_EXPORT
    size(600, 600)
    frameRate(30)
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input()

    Ponto.SET = set()
    NUM_PONTOS = int(input.analog(2) / 4)
    for _ in range(NUM_PONTOS):
        Ponto.SET.add(Ponto(width / 2, height / 2))

def draw():
    background(200)

    TAM_ARESTA = input.analog(1) / 4
    NUM_PONTOS = int(input.analog(2) / 4)
    VEL_MAX = input.analog(3) / 128
    CONNECT_RATE = 0.5 + input.analog(4) / 256  # % of connections

    # para cada ponto
    p_list, r_list = [], []
    for ponto in Ponto.SET:
        ponto.move(VEL_MAX)    # atualiza posição
        p_list.append(ponto)
        r_list.append(ponto.r)
    noFill()
    strokeWeight(3)
    poly_rounded2(p_list, r_list)

    # checa arestas, se OK desenhar, se nãotem pontos removidos ou iguais
    pontos_com_arestas = set()  # para guardar pontos com aresta
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET)\
                or (aresta.p1 is aresta.p2):  # arestas degeneradas
            Aresta.ARESTAS.remove(aresta)   # remove a aresta
        else:                # senão, tudo OK!
            #aresta.desenha()  # desenha a linha
            aresta.puxa_empurra(TAM_ARESTA)  # altera a velocidade dos pontos
            # Adiciona ao conjunto de pontos com aresta
            pontos_com_arestas.update([aresta.p1, aresta.p2])

    pontos_sem_arestas = Ponto.SET - pontos_com_arestas
    # print(len(Ponto.SET), len(pontos_sem_arestas), len(pontos_com_arestas))
    # atualiza número de pontos
    quantidade_atual_de_pontos = len(Ponto.SET)
    if NUM_PONTOS > quantidade_atual_de_pontos:
        Ponto.SET.add(Ponto(random(width), random(height)))
    elif NUM_PONTOS < quantidade_atual_de_pontos - 2:
        if pontos_sem_arestas:
            # remove um ponto sem aresta
            Ponto.SET.remove(pontos_sem_arestas.pop())
        else:
            Ponto.SET.pop()  # remove um ponto qualquer
    # outra maneira de eliminar pontos solitários é criando arestas
    if pontos_sem_arestas:
        for ponto in pontos_sem_arestas:
            ponto.cria_arestas()
    # atualiza número de arestas
    if int((NUM_PONTOS) * CONNECT_RATE) > len(Aresta.ARESTAS) + 1:
        if pontos_sem_arestas:   # preferência por pontos solitários
            choice(list(pontos_sem_arestas)).cria_arestas()
        else:
            choice(list(Ponto.SET)).cria_arestas()
    elif int(NUM_PONTOS * CONNECT_RATE) < len(Aresta.ARESTAS) - 1:
        Aresta.ARESTAS.remove(choice(Aresta.ARESTAS))

    if input.digital(13):
        # Ponto.reset(int(input.analog(2) / 4))
        Ponto.SET = set()
        for _ in range(NUM_PONTOS):
            Ponto.SET.add(Ponto(width / 2, height / 2))

    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 5 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
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
    if key == 'h':
        input.help()

    input.keyPressed()

def keyReleased():
    input.keyReleased()
