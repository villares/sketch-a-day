# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "sketch_190311a"

add_library('GifAnimation')
add_library('peasycam')

from collections import deque
from gif_exporter import gif_export

from graphs import *
from inputs import Input
from arcs import var_bar, bar

history = deque(maxlen=40)

def setup():
    global cam, input, GIF_EXPORT
    size(600, 600, P3D)
    frameRate(30)
    GIF_EXPORT = False
    # 4 sliders if no Arduino library is passed or no board is selected
    input = Input()
    cam = PeasyCam(this, 660)

    Ponto.SET = set()
    NUM_PONTOS = int(input.analog(2) / 4)
    for _ in range(NUM_PONTOS):
        Ponto.SET.add(Ponto(width / 2, height / 2))

def draw():
    background(200)
    translate(-width / 2, -height / 2, 30 * 7)

    TAM_ARESTA = input.analog(1) / 4
    NUM_PONTOS = int(input.analog(2) / 4)
    VEL_MAX = input.analog(3) / 128
    CONNECT_RATE = 0.5 + input.analog(4) / 256  # % of connections
    update_graph(TAM_ARESTA, NUM_PONTOS, VEL_MAX, CONNECT_RATE)

    # para cada ponto
    for ponto in Ponto.SET:
        ponto.move(VEL_MAX)    # atualiza posição

    a_list = [(a.p1.x, a.p1.y, a.p1.cor,
               a.p2.x, a.p2.y, a.p2.cor) for a in Aresta.ARESTAS]
    history.append(a_list)

    for i, layer in enumerate(history):
        translate(0, 0, -10)
        # fill(200 - i * 4)
        for p1x, p1y, p1r, p2x, p2y, p2r in layer:
            fill(lerpColor(p1r, p2r, 0.5))
            bar( p1x, p1y, p2x, p2y)
 
    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 5 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename=SKETCH_NAME)

    # read & draw sliders & checks mouse dragging / keystrokes
    cam.beginHUD()
    input.update()
    cam.endHUD()

# def mouseDragged():        # quando o mouse é arrastado
# for ponto in Ponto.SET:   # para cada Ponto checa distância do mouse
#         if dist(mouseX, mouseY, ponto.x, ponto.y) < 10:
# move o Ponto para posição do mouse
#             ponto.x, ponto.y = mouseX, mouseY
#             ponto.vx = 0
#             ponto.vy = 0

def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()

    input.keyPressed()

    if input.digital(13):  # or spacebar
        Ponto.reset_all(NUM_PONTOS)

def keyReleased():
    input.keyReleased()

def update_graph(TAM_ARESTA, NUM_PONTOS, VEL_MAX, CONNECT_RATE):
    # checa arestas, se OK desenhar, se nãotem pontos removidos ou iguais
    pontos_com_arestas = set()  # para guardar pontos com aresta
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET)\
                or (aresta.p1 is aresta.p2):  # arestas degeneradas
            Aresta.ARESTAS.remove(aresta)   # remove a aresta
        else:                # senão, tudo OK!
            # aresta.desenha()  # desenha a linha
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


# print text to add to the project's README.md
def settings():
    OUTPUT = ".gif"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
