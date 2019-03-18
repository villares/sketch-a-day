# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190317a", ".gif"

"""
Based on sketch_190214a
"""
from collections import namedtuple, deque
import copy as cp
add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from arcs import var_bar, poly_rounded
import random as rnd

SPACING, MARGIN = 100, 100
X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inicial = [], [], []
NUM_NODES = 4  # número de elementos do desenho / number of nodes
Node = namedtuple('Node', 'x y t_size s_weight points_to')
end_mode = False
strips = 10
history = deque(maxlen=40)


def setup():
    global desenho
    smooth(16)
    size(600, 600, P3D)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    cam = PeasyCam(this, 600)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)
    desenho = desenho_atual

def draw():
    global strips, desenho, desenho_atual, outro_desenho, end_mode
    #translate(0, -600)
    #rotateX(HALF_PI / 2)
    translate(-width/2, -height/2)
    background(200)
    fc = frameCount % 100 - 50
    #print(fc)
    
 
    history.append(cp.deepcopy(desenho))
    for i, d in enumerate(history):
        translate(0, 0, -10)
        strips = 10 + 10 * sin((i + frameCount) * TWO_PI / 50.)
        desenho_plot(d)

    # if frameCount > 50:
    #     gif_export(GifMaker, filename=SKETCH_NAME, delay=200)
    #strips += 1

    if fc < 0:
        desenho = desenho_atual
    elif 0 <= fc < 50:
        desenho =  make_inter_nodes(map(fc, 0, 49, 0, 1))
    if fc == 49:
        desenho_atual, outro_desenho = outro_desenho, desenho_atual
        desenho = desenho_atual
        if end_mode:
            exit()
        if frameCount == 100:
            make_nodes_point(outro_desenho)
        else:
            print("will reset")
            end_mode = True
            outro_desenho[:] = cp.deepcopy(desenho_inicial)


def keyPressed():
    global save_frames
    if key == 'g':
        gif_export(GifMaker, filename=SKETCH_NAME)
    if key == 'r':
        make_nodes_point(desenho_atual)
    if key == 'n':
        novo_desenho(desenho_atual)

def novo_desenho(desenho):
    """
    esvazia a lista elementos (setas e linhas) do desenho anterior
    clears the list of nodes and creates a a new drawing appending desenho_atual,
    a list of nodes/drawing elements: specials, connecting lines and lonely nodes
    """
    desenho[:] = []
    for _ in range(NUM_NODES):
        desenho.append(new_node())
    make_nodes_point(desenho)
    outro_desenho[:] = cp.deepcopy(desenho)
    make_nodes_point(outro_desenho)


def new_node():
    return Node(                   # elemento/"nó" uma namedtuple com:
        rnd.choice(X_LIST),        # x
        rnd.choice(Y_LIST),        # y
        rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
        rnd.choice([2, 4, 6]),     # s_weight
        []  # points_to... (lista com ref. a outro elem.))
    )

def make_nodes_point(desenho):
    for node in desenho:  # para cada elemento do desenho
        node.points_to[:] = []
        node.points_to.append(new_node())
        node.points_to.append(new_node())

def desenho_plot(d):
    for node in d:
        p1, p2 = node.points_to  # se estiver apontando para alguém
        # strokeWeight(node.s_weight)
        with pushMatrix():
            for i in range(2):
                c = 128 + 128 * sin(frameCount * TWO_PI / 50. + PI * i)
                #print(c)
                stroke(c)
                strokeWeight(2)
                translate(0, 0, node.s_weight)
                poly_rounded([node, p1, p2], (node.s_weight + i) * strips)

# def mouseWheel(E):
#     global strips
#     strips += int(E.getAmount())
#     print(strips)

def make_inter_nodes(amt):
    desenho_inter = []
    for n1, n2 in zip(desenho_atual, outro_desenho):
        desenho_inter.append(Node(                   # elemento/"nó" uma namedtuple com:
            n1.x,        # x
            n1.y,        # y
            n1.t_size,  # t_size (tail/circle size)
            n1.s_weight,     # s_weight (espessura da linha)
            [PVector(lerp(p1.x, p2.x, amt), lerp(p1.y, p2.y, amt))
             for p1, p2 in zip(n1.points_to, n2.points_to)]
        ))
    return desenho_inter

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
