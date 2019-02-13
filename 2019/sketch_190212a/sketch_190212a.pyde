# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190212a", ".gif"

"""
New rounded poly take
"""
from collections import namedtuple
import copy as cp
add_library('GifAnimation')
from gif_exporter import gif_export
#add_library('peasycam')
from arcs import var_bar, poly_rounded
import random as rnd

SPACING, MARGIN = 100, 100
X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inter, desenho_inicial = [], [], [], []
NUM_NODES = 4  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', 'x y t_size s_weight is_special points_to')
save_frames = False

def setup():
    smooth(16)
    size(600, 600)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    #cam = PeasyCam(this, 500)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)
    println("'s' to save, and 'n' for a new drawing")

def keyPressed():
    global save_frames
    if key == 'g':
        gif_export(GifMaker, filename=SKETCH_NAME)
        # saveFrame("####.png")
        # save_frames = not save_frames
        # print "Saving "+repr(save_frames)
    if key == 'r':
        make_nodes_point(desenho_atual)
    if key == 'n':
        novo_desenho(desenho_atual)
    if key == ' ':
        background(200)

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
        # rnd.choice([True, False]),  # is_special? (se é seta ou 'linha')
        True,
        []  # points_to... (lista com ref. a outro elem.))
    )

def make_nodes_point(desenho):
    for node in desenho:  # para cada elemento do desenho
        node.points_to[:] = []
        node.points_to.append(new_node())
        node.points_to.append(new_node())


def draw():
    #translate(-width/2, -height/2)
    global desenho_atual, outro_desenho
    background(0)
    # fc = frameCount % 300 - 150
    # if fc < 0:
    #     desenho = desenho_atual
    # elif 0 <= fc < 149:
    #     # if frameCount % 10 == 0:.
    #     make_inter_nodes(map(fc, 0, 150, 0, 1))
    #     desenho = desenho_inter
    # elif fc == 149:
    #     desenho_atual, outro_desenho = outro_desenho, desenho_atual
    #     desenho = desenho_atual
    #     if not mousePressed:
    #         make_nodes_point(outro_desenho)
    #         print("will reset")
    #     else:
    #         outro_desenho[:] = cp.deepcopy(desenho_inicial)

    # then draws black specials
    for node in desenho_atual:
            p1, p2 = node.points_to  # se estiver apontando para alguém
            # strokeWeight(node.s_weight)
            with pushMatrix():
                for i in range(-1, 2):
                    stroke(128 + i * 64, 200, 200)
                    translate(0, 0, node.s_weight)
                    poly_rounded([node, p1, p2], (node.s_weight + i)* 5)


    #if frameCount % 4 == 0:
        #saveFrame("####.tga")


# def make_inter_nodes(amt):
#     desenho_inter[:] = []
#     for n1, n2 in zip(desenho_atual, outro_desenho):
#         if n1.points_to:
#             p1x, p1y = n1.points_to[0].x, n1.points_to[0].y
#         else:
#             p1x, p1y = n1.x, n1.y
#         if n2.points_to:
#             p2x, p2y = n2.points_to[0].x, n2.points_to[0].y
#         else:
#             p2x, p2y = n2.x, n2.y
#         desenho_inter.append(Node(                   # elemento/"nó" uma namedtuple com:
#             n1.x,        # x
#             n1.y,        # y
#             n1.t_size,  # t_size (tail/circle size)
#             n1.s_weight,     # s_weight (espessura da linha)
#             n1.is_special,  # is_special? (se é barra ou 'linha')
#             # cp.deepcopy(n1.points_to)
#             [PVector(lerp(p1x, p2x, amt), lerp(p1y, p2y, amt))]
#         ))

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
